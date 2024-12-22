from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import CustomUser

class UserTests(APITestCase):
    def test_user_registration(self):
        """
        Test that a user can register successfully.
        """
        url = reverse('user-register')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])

    def test_user_login(self):
        """
        Test that a user can log in with correct credentials.
        """
        # Register the user
        self.client.post(reverse('user-register'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword',
        }, format='json')

        
        user = CustomUser.objects.filter(username='testuser').first()
        assert user is not None, "User was not created in the test database"
        assert user.check_password('securepassword'), "Password was not hashed correctly"

        # Try logging in
        url = reverse('user-login')
        data = {
            'username': 'testuser',
            'password': 'securepassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Login successful!')

    def test_user_login_invalid_credentials(self):
        """
        Test that login fails with invalid credentials.
        """
        url = reverse('user-login')  # Use the correct URL name for login
        data = {
            'email': 'invalid@example.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Invalid credentials')
