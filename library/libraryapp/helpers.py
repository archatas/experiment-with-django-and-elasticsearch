# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.functional import LazyObject


class SearchResults(LazyObject):
    def __init__(self, search_object):
        self._wrapped = search_object

    def __len__(self):
        return self._wrapped.count()

    def __getitem__(self, index):
        search_results = self._wrapped[index]
        if isinstance(index, slice):
            search_results = list(search_results)
        return search_results


class DateInput(forms.DateInput):
    input_type = 'date'
