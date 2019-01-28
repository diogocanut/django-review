from django.test import TestCase
from rest_framework import status
from rest_auth.tests.mixins import TestsMixin
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Review


class TestViewSets(TestsMixin, TestCase):

    USERNAME = 'person11'
    PASS = 'person11'
    FIRST_NAME = 'person'
    LAST_NAME = 'person'

    REGISTRATION_DATA = {
        "username": USERNAME,
        "password1": PASS,
        "password2": PASS,
        "first_name": FIRST_NAME,
        "last_name": LAST_NAME,
    }

    payload = {
        "username": USERNAME,
        "password": PASS
    }

    def init(self):
        self.login_url = reverse('rest_login')
        self.logout_url = reverse('rest_logout')
        self.register_url = reverse('rest_register')

    def login(self):
        self.post(self.login_url, data=self.payload, status_code=status.HTTP_200_OK)

    def logout(self):
        self.post(self.logout_url, status=status.HTTP_200_OK)

    def setUp(self):
        self.init()

    def test_get_query_with_no_login(self):
        resp = self.get('/reviews/', status_code=403)
        self.assertEqual(resp.json['detail'], u'Authentication credentials were not provided.')

    def test_registration(self):
        user_count = User.objects.all().count()

        self.post(self.register_url, data={}, status_code=400)
        result = self.post(self.register_url, data=self.REGISTRATION_DATA, status_code=201)
        self.assertIn('key', result.data)
        self.assertEqual(User.objects.all().count(), user_count + 1)

        new_user = User.objects.latest('id')
        self.assertEqual(new_user.username, self.REGISTRATION_DATA['username'])

    def test_get_query_with_login(self):
        user = User.objects.create_user(self.USERNAME, '', self.PASS)

        self.login()
        self.post(self.login_url, data=self.payload, status_code=status.HTTP_200_OK)

        resp = self.get('/reviews/', status_code=status.HTTP_200_OK)
        self.assertEqual(resp.json, [])

        review = Review.objects.create(
            user=user,
            rating='3',
            title='teste',
            summary='teste',
        )
        resp = self.get('/reviews/', status_code=status.HTTP_200_OK)
        self.assertEqual(resp.json[0]['user']['username'], user.username)

    def test_get_query_other_users(self):
        user = User.objects.create_user(self.USERNAME, '', self.PASS)
        user_test = User.objects.create_user('tester11', '', 'tester11')

        self.login()
        self.post(self.login_url, data=self.payload, status_code=status.HTTP_200_OK)                

        review = Review.objects.create(
            user=user_test,
            rating='3',
            title='teste',
            summary='teste',
        )

        resp = self.get('/reviews/', status_code=status.HTTP_200_OK)
        self.assertEqual(resp.json, [])


    def test_get_query_superuser(self):
        user = User.objects.create_superuser(self.USERNAME, '', self.PASS, )
        user_test = User.objects.create_user('tester11', '', 'tester11')

        self.login()
        self.post(self.login_url, data=self.payload, status_code=status.HTTP_200_OK)                

        review = Review.objects.create(
            user=user_test,
            rating='3',
            title='teste',
            summary='teste',
        )

        resp = self.get('/reviews/', status_code=status.HTTP_200_OK)
        self.assertEqual(resp.json[0]['user']['username'], user_test.username)

    def test_post_with_ipaddr(self):

        user = User.objects.create_user(self.USERNAME, '', self.PASS)
        rev_payload = {
            "rating": "3",
            "title": "teste",
            "summary": "teste",        
        }

        self.login()
        self.post(self.login_url, data=self.payload, status_code=status.HTTP_200_OK)

        self.post(
            '/reviews/',
            data=rev_payload,
            status_code=status.HTTP_201_CREATED,
            REMOTE_ADDR="127.0.0.1"
        )

        resp = self.get('/reviews/', status_code=status.HTTP_200_OK)

        self.assertEqual(resp.json[0]['ip_address'], "127.0.0.1")
