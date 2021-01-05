Shoyo Graphql API
====================


Setting Up
^^^^^^^^^^^^^^^^^^^^^

* To get started, Install requirmeents, run migrations and visit graphql route.

* Included makefile requires following environment variables. Ensure you have them in your .env if you want to use make::

    $ PYTHON=python3 APP_DOR=. BIN=env/bin


* To run migrations, use this command::

    $ python manage.py migrate or make migrate

* To run server, use this command::

    $ python manage.py runserver or make run

* To visit graphql route, use this url::

    $ http://localhost:8000/graphql



