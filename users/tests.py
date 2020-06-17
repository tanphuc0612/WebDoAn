from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
from django.test import Client
# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='duc_v10', password='duc_dep_trai')
        User.objects.create(username='duc_v20', password='duc_soai_ca')
    
    def test_profile(self):
        """Username of Profiles must have the same name with Username of User"""
        profile_v10 = User.objects.get(username='duc_v10').profile
        profile_v20 = User.objects.get(username='duc_v20').profile
        self.assertEqual(profile_v10.__str__(), 'Profile: duc_v10')
        self.assertEqual(profile_v20.__str__(), 'Profile: duc_v20')

class LoginTest(TestCase):
    def setUp(self):
        self.anonymous = {
            'username': 'duc_v30',
            'password': 'duc_dep_trai'
        }
        user = User.objects.create_user(**self.anonymous)

    def test_login(self):
        client = Client()
        logged_in = client.login(**self.anonymous)
