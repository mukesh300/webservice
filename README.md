#### FLASK REST BOILER-PLATE WITH JWT

## Want to use this project?

### Basics

1. Fork/Clone
1. Activate a virtualenv
1. Install the requirements

### Create the tables and run the migrations:
```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
```


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.
