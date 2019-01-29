## Running the project:

    1. Clone this repo

    2. Create a virtualenv with python 3.6 and activate it:
        virtualenv djangoreview --python=python3.6
        source djangoreview/bin/activate

    3. Create a database named djangoreview and change the project settings with your postgres user and password
        su postgres
        psql
        CREATE DATABASE djangoreview;
        

    4. Install requirements
        cd djangoreview
        pip install -r requirements.txt

    5. Run migrations
        python manage.py migrate

    6. Create a superuser.
        python manage.py createsuperuser

    7. Run server
        python manage.py runserver

    Now the server is running in localhost.

## Usage: 

    Registration with django rest-auth on url /rest-auth/registration

    Login on /rest-auth/login

    Logout on /rest-auth/logout

    The review api is on /reviews

    Only logged in users can post reviews, a GET method on /reviews will only return the reviews submitted by the logged user, except for the superuser, that can receive all the reviews.
