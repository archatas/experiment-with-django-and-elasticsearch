# Experiment with Django and Elasticsearch

This Django project explores the possibilities of full-text search and filtering using Elasticsearch.

## Dependencies

The project depends on:

- [Django](https://www.djangoproject.com/) ≥ 1.8
- [Elasticsearch](https://www.elastic.co/products/elasticsearch) v6.2 - Server
- [elasticsearch](https://github.com/elastic/elasticsearch-py) v6.2 - Python Elasticsearch Client
- [elasticsearch-dsl](https://elasticsearch-dsl.readthedocs.io/en/latest/) v6.1 - Higher level library for the search queries
- [django-elasticsearch-dsl](https://github.com/sabricot/django-elasticsearch-dsl) v0.5.0 - Integration with Django package
- several other modules listed in the requirements.txt

## Quickstart

1. Install and run Elasticsearch server. For example on macOS:

    ```
    $ brew install elasticsearch
    $ brew services start elasticsearch
    ```

2. Clone this project

3. Create a virtual environment, activate it, and install Python dependencies

    - If you use pipenv, go to project's directory and run:

        ```
        $ mkdir .venv
        $ pipenv install
        $ pipenv shell
        ```

    - Otherwise, proceed the good old way:

        ```
        $ virtualenv venv
        $ source venv/bin/activate
        (venv)$ pip install -r requirements.txt
        ```

4. Build the search index for the database:

    ```
    (venv)$ python manage.py search_index --rebuild
    ```

5. Run local webserver:

    ```
    (venv)$ python manage.py runserver
    ```

6. Open http://127.0.0.1:8000 to play around with the search.
