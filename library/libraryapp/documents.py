# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django_elasticsearch_dsl import DocType, Index, fields
from .models import Author, Book

# Name of the Elasticsearch index
search_index = Index('library')
# See Elasticsearch Indices API reference for available settings
search_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@search_index.doc_type
class BookDocument(DocType):
    authors = fields.NestedField(properties={
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'author_name': fields.TextField(),
        'pk': fields.IntegerField(),
    }, include_in_root=True)

    isbn = fields.KeywordField()

    class Meta:
        model = Book # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'publishing_date',
        ]
        related_models = [Author]

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Book instance(s) from the related model."""
        if isinstance(related_instance, Author):
            return related_instance.book_set.all()
