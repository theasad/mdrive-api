from django.db import models


class FolderQuerySet(models.QuerySet):

    # Get only parent folder
    def parents(self):
        return self.filter(parent__isnull=True)

    # Get only child folder
    def children(self):
        return self.filter(parent__isnull=False)


class FileQuerySet(models.QuerySet):
        # Get only parent folder
    def root_files(self):
        return self.filter(folder__isnull=True)
