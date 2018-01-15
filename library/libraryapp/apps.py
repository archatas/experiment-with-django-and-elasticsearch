# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LibraryAppConfig(AppConfig):
    name = 'library.libraryapp'
    verbose_name = _("Library")

    def ready(self):
        pass
