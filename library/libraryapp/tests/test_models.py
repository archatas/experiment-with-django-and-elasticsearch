# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils.text import force_text

from ..models import MyModel


class MyModelModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(MyModelModelTest, cls).setUpClass()
        cls.instance = MyModel.objects.create(title="Test")
    
    @classmethod
    def tearDownClass(cls):
        super(MyModelModelTest, cls).tearDownClass()
        cls.instance.delete()

    def test_str(self):
        self.assertEqual(
            force_text(self.instance),
            "Test",
            "The __str__ value doesn't match",
        )
