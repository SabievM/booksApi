web: gunicorn BooksAPI.wsgi --log-file -
#or works good with external database
web: python manage.py migrate && gunicorn BooksAPI.wsgi