# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# from users.models import User

# class UserAuthTests(APITestCase):

#     def test_user_registration(self):
#         # Simulate user registration
#         url = reverse('signup')  # Updated to 'signup'
#         data = {
#             "username": "testclient",
#             "password": "testpassword123",
#             "email": "client@example.com",
#             "role": "client"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         # Print the user creation for debugging
#         user = User.objects.get(username='testclient')
#         print(f"Username: {user.username}, Email: {user.email}, Active: {user.is_active}")

#         self.assertTrue(User.objects.filter(username='testclient').exists())

#     def test_user_login(self):
#         # Simulate user registration
#         url = reverse('signup')  # Updated to 'signup'
#         registration_data = {
#             "username": "testclient",
#             "password": "testpassword123",
#             "email": "client@example.com",
#             "role": "client"
#         }
#         registration_response = self.client.post(url, registration_data, format='json')
#         self.assertEqual(registration_response.status_code, status.HTTP_201_CREATED)

#         # Verify user is active
#         user = User.objects.get(email='client@example.com')
#         self.assertTrue(user.is_active)

#         # Now attempt to log in with the correct credentials using JWT
#         url = reverse('jwt_create')
#         login_data = {
#             "email": "client@example.com",
#             "password": "testpassword123"
#         }
#         response = self.client.post(url, login_data, format='json')

#         # Print the login response for debugging
#         print(f"Login response: {response.data}")

#         # Check if the login was successful
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('access', response.data)
#         self.assertIn('refresh', response.data)