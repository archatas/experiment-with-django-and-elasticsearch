# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last name')),
                ('author_name', models.CharField(max_length=200, verbose_name='Author name')),
            ],
            options={
                'ordering': ('author_name',),
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('authors', models.ManyToManyField(to='libraryapp.Author', verbose_name='Authors')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
