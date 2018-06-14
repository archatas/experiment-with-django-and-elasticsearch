# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_book_publishing_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=20, verbose_name='ISBN', blank=True),
        ),
    ]
