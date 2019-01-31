API endpoints
=============

Login
-----

- /v1/rest-auth/login/ (POST)

    - username
    - password

    Returns Token key

- /v1/rest-auth/logout/ (POST)


Registration
------------

- /v1/rest-auth/registration/ (POST)

    - username
    - password1
    - password2
    - email
    - first_name
    - last_name


Reviews
---------------------------

    Only for logged users.

- /v1/rest-auth/reviews/ (GET)
    Returns id, user, rating, title, summary, sub_date, ip_address, company_name

- /v1/rest-auth/reviews/ (POST)

    - rating (1-5)
    - title
    - summary
    - company_name
