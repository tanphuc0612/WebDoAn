from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='duc_v10', password='duc_dep_trai')
        User.objects.create(username='duc_v20', password='duc_soai_ca')
    
    def test_profile(self):
        profile_v10 = User.objects.get(username='duc_v10').profile
        profile_v20 = User.objects.get(username='duc_v20').profile
        self.assertEqual(profile_v10.__str__(), 'Profile: duc_v10')
        self.assertEqual(profile_v20.__str__(), 'Profile: duc_v20')

