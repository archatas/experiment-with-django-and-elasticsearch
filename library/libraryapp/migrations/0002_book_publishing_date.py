# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publishing_date',
            field=models.DateField(null=True, verbose_name='Publishing date', blank=True),
        ),
    ]
