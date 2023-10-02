from django.db import models

from filer.models import File


class RefreshFile(models.Model):
    """Refresh file from URL."""

    file = models.OneToOneField(File, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        folder = f'{self.file.folder}/' if self.file.folder else ""
        return f'{self.url} → {folder}{self.file}'
