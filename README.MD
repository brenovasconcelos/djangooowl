# HOW TO SETUP AND TEST API

first of all, use the following command to run the script and load users on db:

**_python3 manage.py import_customers_**
(can take a few minutes)

after, run the command:

**_python3 manage.py runserver_**

on http://127.0.0.1:8000/swagger/ you will be able to test the API.

In the /user/{user_id}/ endpoint, send a number as param

## Automated Tests

If you want to run the tests, just use **_python manage.py test_**
