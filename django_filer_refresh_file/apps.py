from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FilerRefreshConfig(AppConfig):
    name = 'django_filer_refresh_file'
    verbose_name = _("Filer refresh file")
