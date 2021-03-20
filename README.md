# InfoMarket Challenge

This is a technical challenge proposed by the [InfoMarket](https://infomarketpesquisa.com/) company. The challenge is to build a simple CRUD in any language and using any relational database. As a personal choice, I preferred to use the Flask microframework in Python and the PostgreSQL database.

The CRUD involves two models:
- An User model containing the user's name and user's age
- An Adddress model containing information about the user's address: street, number, city, state

The relationship between User and Address is One-To-One.

The FlaskSQLAlchemy library is a flask extension that makes it easier to use SQLAlchemy ORM and facilitate the execution of migrations.

A simple web application was built using pure HTML, CSS and Javascript to consume the API.

## Libraries and tools used

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [FlaskSQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [CORS](https://flask-cors.readthedocs.io/en/latest/)
- [PostgreSQL](https://www.postgresql.org/)
- [Fetch](https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API/Using_Fetch)
- [Async/Await](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/async_function)
- [PEP8](https://www.python.org/dev/peps/pep-0008/)

## Dependencies

- [Python3.x](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)

## How to run

### Install and configure PostgreSQL

The tutorial below refers to Unix-based systems.

First, you have to download and configure the PostgreSQL database. After that, create a superuser:

```
sudo -u postgres createuser --superuser username
```

After, create a database using the created user account:

```
sudo -u username createdb database_name
```

Now, you can access the created database:

```
psql -U username -d database_name
```

**All tutorials below, you must enter the backend folder.**

### Install python dependencies


You can install the dependencies in two ways:

1. Using pipenv:

    ```
    pipenv install
    ```

2. Using pip3:

    ```
    pip3 install -r requirements.txt
    ```

### Configure environment variables

You need to create an .env file following the .env.example file.

```
APP_SETTINGS=
DATABASE_URL=
```

The APP_SETTINGS variable can be:

- config.config.DevelopmentConfig for development
- config.config.ProductionConfig for production
- config.config.StagingConfig for staging
- config.config.TestingConfig for testing

The DATABASE_URL variable is your database url. If you are using in localhost, the URL is something like: `postgresql:///database_name`.

### Run migrations

1.  ```
    python manage.py db init
    ```

2.  ```
    python manage.py db migrate
    ```

3.  ```
    python manage.py db upgrade
    ```

### Run the server

```
python manage.py runserver
```

The server will be running on `http://127.0.0.1:5000/`

### Frontend

You can just open the index.html file in the browser or you can run:

```
python -m http.server 5500
```

## API Endpoints

- [GET users](docs/get_users.md)
- [GET users/:id](docs/get_user.md)
- [POST users/](docs/post_user.md)
- [PUT users/:id](docs/put_user.md)
- [DELETE users/:id](docs/delete_user.md)

## TODO

- [x] Validate the parameters and body passed in all routes.
- [ ] Log API exceptions
- [x] Refactor blueprints (separate handlers from db manipulation)
- [x] Bug: Investigate delete operation on index.html page
- [ ] Add unit tests