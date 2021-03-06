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
        queryset = Folder.objects.all()
        return queryset


class DriveFileViewSet(generics.ListCreateAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        order_by = self.request.GET.get('orderby')
        query_set = File.objects.root_files().order_by(
            order_by if order_by else '-created')
        return query_set


class FolderFileViewSet(generics.ListCreateAPIView):

    serializer_class = FileSerializer

    def get_folder_obj(self, slug):

        try:
            return Folder.objects.get(slug=slug)
        except Folder.DoesNotExist:
            raise Http404

    def get_queryset(self):
        order_by = self.request.GET.get('orderby')
        slug = self.kwargs.get('folder_slug')
        if slug:
            folder = self.get_folder_obj(slug)
            query_set = folder.files.all().order_by(order_by if order_by else '-created')
        else:
            query_set = File.objects.root_files().order_by(
                order_by if order_by else '-created')
        return query_set
