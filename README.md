# Experiment with Django and Elasticsearch

This Django project explores the possibilities of full-text search and filtering using Elasticsearch.

## Dependencies

The project depends on:

- [Django](https://www.djangoproject.com/) ≥ 1.8
- [Elasticsearch](https://www.elastic.co/products/elasticsearch) 5.6 - Server
- [elasticsearch](https://github.com/elastic/elasticsearch-py) v5.5.1 - Python Elasticsearch Client
- [elasticsearch-dsl](https://elasticsearch-dsl.readthedocs.io/en/latest/) v5.4.0 - Higher level library for the search queries
- [django-elasticsearch-dsl](https://github.com/sabricot/django-elasticsearch-dsl) v0.4.4 - Integration with Django package
- several other modules listed in the requirements.txt

## Quickstart

1. Install and run Elasticsearch server. For example on macOS:

    ```
    $ brew install elasticsearch@5.6
    $ brew services start elasticsearch@5.6
    ```

2. Create and activate a virtual environment:

    ```
    $ virtualenv venv
    $ . venv/bin/activate
    ```
 
3. Clone this project

4. Install pip requirements into the virtual environment:

    ```
    (venv)$ pip install -r requirements.txt
    ```

5. Build the search index for the database:

    ```
    (venv)$ python manage.py search_index --rebuild
    ```

6. Run local webserver:

    ```
    (venv)$ python manage.py runserver
    ```

7. Open http://127.0.0.1:8000 to play around with the search.
