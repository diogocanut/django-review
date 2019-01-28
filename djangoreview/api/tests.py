from django.test import TestCase
from rest_framework import status
from rest_auth.tests.mixins import TestsMixin
from django.contrib.auth.models import User
from django.urls import reverse


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

    def setUp(self):
        self.init()

    # def test_get_query_with_no_login(self):
    #     resp = self.get(self.login_url, status_code=200)


    def test_registration(self):
        user_count = User.objects.all().count()

        self.post(self.register_url, data={}, status_code=400)
        result = self.post(self.register_url, data=self.REGISTRATION_DATA, status_code=201)
        self.assertIn('key', result.data)
        self.assertEqual(User.objects.all().count(), user_count + 1)

        new_user = User.objects.latest('id')
        self.assertEqual(new_user.username, self.REGISTRATION_DATA['username'])

    def login(self):
        self.post(self.login_url, data=self.payload, status_code=status.HTTP_200_OK)

    # def test_get_query_not_superuser(self):

    #     resp = self.post(self.login_url, data=self.payload, status_code=400)
    #     self.assertEqual(resp.json['non_field_errors'][0], u'Must include "email" and "password".')

    def logout(self):
        self.post(self.logout_url, status=status.HTTP_200_OK)