# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import template

register = template.Library()

@register.filter
def get_relevance_score(item):
    return item._score