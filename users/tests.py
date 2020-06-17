from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
from django.test import Client
# Create your tests here.

class ProfileTestCase(TestCase):
    id_1 = {
        'username' : 'duc_v10',
        'password' : 'duc_dep_trai',
    }
    def setUp(self):
        duc_v10 = User.objects.create_user(**self.id_1)
    
    def test_exist_profile(self):
        profile_v10 = User.objects.get(username=self.id_1['username']).profile
        self.assertEqual(profile_v10.__str__(), f"Profile: {self.id_1['username']}")

    def test_profile_view(self):
        client = Client()
        logged_in = client.login(**self.id_1)
        if logged_in:
            id_user = client.session['_auth_user_id']
            response = client.get(f"/profile/{id_user}/")
            self.assertEqual(response.status_code, 200)

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
        self.assertTrue(logged_in)

    def test_login_fail(self):
        anonymous_user = {
            'username' : 'duc_xau_trai',
            'password' : 'leu_leu'
        }
        client = Client()
        logged_in = client.login(**anonymous_user)
        self.assertTrue(not logged_in)
    