from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
# Create your tests here.

class AccountsURLTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='Faaiz',
            last_name='Ali',
            email='faaizalitariq@gmail.com',
            username='faaiz',
            password='Pak123pak',
        )
    def test_registration_url(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_url(self):
        data = {'username':'faaiz','password':'Pak123pak'}
        response = self.client.post(reverse('accounts:login'), data, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_profile_url(self):
        response = self.client.get(reverse('accounts:profile'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "is")