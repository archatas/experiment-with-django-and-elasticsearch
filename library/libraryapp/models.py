# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(_("First name"), max_length=200)
    last_name = models.CharField(_("Last name"), max_length=200)
    author_name = models.CharField(_("Author name"), max_length=200)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        ordering = ("author_name",)

    def __str__(self):
        return self.author_name


@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    authors = models.ManyToManyField(Author, verbose_name=_("Authors"))
    publishing_date = models.DateField(_("Publishing date"), blank=True, null=True)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ("title",)

    def __str__(self):
        return self.title
