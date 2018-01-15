# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ["author_name"]
    list_filter = ["book"]
    search_fields = ["first_name", "last_name", "author_name"]
    fieldsets = [
        (_("Content"), {'fields': ["first_name", "last_name", "author_name"]}),
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ["title", "publishing_date"]
    list_filter = ["authors"]
    search_fields = ["title",]
    fieldsets = [
        (_("Content"), {'fields': ["title", "authors", "publishing_date"]}),
    ]
    filter_horizontal = ["authors"]