from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .forms import RefreshFileForm


class RefreshFileAdmin(admin.ModelAdmin):
    """RefreshFile Admin."""

    list_display = ["url", "file", "view_file_folder"]

    form = RefreshFileForm

    @admin.display(empty_value="[root]", description=_("Folder"))
    def view_file_folder(self, obj):
        return obj.file.folder

    def get_form(self, request, obj=None, change=False, **kwargs):
        """Get form class with request."""
        form = super().get_form(request, obj=None, change=False, **kwargs)
        form.request = request
        return form
