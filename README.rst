===============================
hangman
===============================

A hangman demo



Start the API
-------------

First, set your app's secret key as an environment variable. For example,
add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export SECRET_KEY='something-really-secret'

Run the following commands to bootstrap your environment ::

    git clone https://github.com/brettatoms/hangman
    cd hangman
    pip install -r requirements/dev.txt

You will see a pretty welcome screen.

In general, before running shell commands, set the ``FLASK_APP`` and
``FLASK_DEBUG`` environment variables ::

    export FLASK_APP=autoapp.py
    export FLASK_DEBUG=1

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade
    flask run


Start the front end server
--------------------------

By default the front end uses the production API.  To have it use the local API edit`game.service.ts` and `auth.service.ts`;

To install the dependencies and start the development front end server ::

    cd frontend
    npm i
    npm run start



Deployment
----------

To deploy the backend ::

    git push heroku master

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``ProdConfig`` is used.


To deploy the backend ::

    npm run build
    npm run deploy


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run the backend tests tests, run ::

    flask test

To run the frontend tests tests, run ::

    cd frontend
    npm run test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.
