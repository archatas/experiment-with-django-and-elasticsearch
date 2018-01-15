# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from ..models import MyModel


class MyModelListViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(MyModelListViewTest, cls).setUpClass()
        cls.instance = MyModel.objects.create(title="Test")
    
    @classmethod
    def tearDownClass(cls):
        super(MyModelListViewTest, cls).tearDownClass()
        cls.instance.delete()

    def test_get(self):
        response = self.client.get('/mymodels/')
        self.assertEqual(
            response.status_code,
            200,
            "Response code is invalid",
        )


class MyModelDetailViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(MyModelDetailViewTest, cls).setUpClass()
        cls.instance = MyModel.objects.create(title="Test")
    
    @classmethod
    def tearDownClass(cls):
        super(MyModelDetailViewTest, cls).tearDownClass()
        cls.instance.delete()

    def test_get(self):
        response = self.client.get('/mymodels/{}/'.format(self.pk))
        self.assertEqual(
            response.status_code,
            200,
            "Response code is invalid",
        )
