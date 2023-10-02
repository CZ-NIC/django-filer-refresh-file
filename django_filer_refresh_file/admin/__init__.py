from django.contrib import admin

from ..models import RefreshFile
from .options import RefreshFileAdmin


admin.site.register(RefreshFile, RefreshFileAdmin)
