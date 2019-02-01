## Running the project:

    1. Clone this repo

    2. Create a virtualenv with python 3.6 and activate it:
        virtualenv djangoreview --python=python3.6
        source djangoreview/bin/activate

    3. Create a database named djangoreview
        su postgres
        psql
        CREATE DATABASE djangoreview;
        
    4. Change the project settings with your postgres user and password.
    
    5. Install requirements
        cd djangoreview
        pip install -r requirements.txt

    6. Run migrations
        python manage.py migrate

    7. Create a superuser.
        python manage.py createsuperuser

    8. Run server
        python manage.py runserver

    Now the server is running, you can go to localhost:8000/ in your browser.

## Usage: 

    Registration with django rest-auth on url localhost:8000/rest-auth/registration/

    Login on localhost:8000/v1/rest-auth/login/

    Logout on localhost:8000/v1/rest-auth/logout/

    The review api is on localhost:8000/v1/reviews/

    Only logged in users can post reviews, a GET method on localhost:8000/v1/reviews/ will only return the reviews submitted by the logged user, except for the superuser, that can receive all the reviews.
