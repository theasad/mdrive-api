import os
import shutil
import tempfile
from fileinput import filename
from pathlib import Path

from django.conf import settings
from django.http import Http404
from django.template.defaultfilters import first
from rest_framework import generics, status
from rest_framework.response import Response

from apps.drive.models import File, Folder
from apps.drive.serializers import (ChildFolderSerializer, FileSerializer,
                                    FolderSerializer)
from backend.settings import MEDIA_ROOT


class FolderViewSet(generics.ListCreateAPIView):
    queryset = Folder.objects.parents()
    serializer_class = FolderSerializer


class FolderDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ChildFolderSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Folder.objects.all()


class DriveFileViewSet(generics.ListCreateAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        order_by = self.request.GET.get('orderby')
        return File.objects.root_files().order_by(order_by or '-created')


class FolderFileViewSet(generics.ListCreateAPIView):

    serializer_class = FileSerializer

    def get_folder_obj(self, slug):

        try:
            return Folder.objects.get(slug=slug)
        except Folder.DoesNotExist:
            raise Http404

    def get_queryset(self):
        order_by = self.request.GET.get('orderby')
        if slug := self.kwargs.get('folder_slug'):
            folder = self.get_folder_obj(slug)
            return folder.files.all().order_by(order_by or '-created')
        else:
            return File.objects.root_files().order_by(order_by or '-created')
