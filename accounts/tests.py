from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from .models import User



def user_login():
    client = APIClient()
    data = {
        "email": "admin@gmail.com",
        "password": "12345"
    }
    
    response = client.post(path=reverse("token_obtain_pair"), data=data)
    access_token = response.json()['data']['access']
    refresh_token = response.json()['data']['refresh']
    return access_token, refresh_token


class AcountsAPIViewTestCase(APITestCase):
    
    def setUp(self):
        self.email = "admin@gmail.com"
        self.password = "12345"
        
        

        self.user = User.objects.create_user(
            self.email, self.password
        )
        self.access_token, self.refresh_token = self.user_login()
        
        self.test_login_success()
        
    def user_login(self):
        data = {
            "email": self.email,
            "password": self.password
        }
        
        response = self.client.post(path=reverse("token_obtain_pair"), data=data)
        access_token = response.json()['data']['access']
        refresh_token = response.json()['data']['refresh']
        return access_token, refresh_token
    
    def test_login_success(self):
        """
        Test to verify login success
        """
        data = {
            "email": self.email,
            "password": self.password
        }
        
        response = self.client.post(path=reverse("token_obtain_pair"), data=data)
        self.access_token = response.json()['data']['access']
        self.refresh_token = response.json()['data']['refresh']
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['code'])
        self.assertEqual(True, response.json()['status'])
        
    
    def test_logout_success(self):
        """
        Test to verify login success
        """
        data = {
            "refresh": self.refresh_token
        }
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(path=reverse("auth_logout"), data=data)
        self.assertEqual(205, response.status_code)
        
    def test_logout_all_device_success(self):
        """
        Test to verify login success
        """
        data = {}
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(path=reverse("auth_logout_all"), data=data)
        self.assertEqual(205, response.status_code)
        
    def test_login_failed_by_wrong_email(self):
        """
        Test to verify login failed
        """
        data = {
            "email": "noemail@gmail.com",
            "password": self.password
        }
        
        response = self.client.post(path=reverse("token_obtain_pair"), data=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(400, response.json()['code'])
        self.assertEqual(False, response.json()['status'])
        
    def test_access_token_by_refresh_success(self):
        """
        Test to verify login success
        """
        
        
        data = {
            "refresh": self.refresh_token,
        }
        
        response = self.client.post(path=reverse("token_refresh"), data=data)

        self.assertEqual(200, response.status_code)
    
        
    def test_admin_registration_success(self):
        """
        Test to verify login success
        """
        data = {
            "email":"admin1@gmail.com",
            "phone_number":"0000000000",
            "address":"US",
            "user_type":"admin",
            "password":"12345"
        }
        
        response = self.client.post(path=reverse("registration"), data=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['code'])
        self.assertEqual(True, response.json()['status'])
        
    def test_admin_registration_failed(self):
        """
        Test to verify login success
        """
        data = {
            "email":"admin1@gmail.com",
            "phone_number":"0000000000",
            "address":"US",
            "password":"12345"
        }
        
        response = self.client.post(path=reverse("registration"), data=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(400, response.json()['code'])
        self.assertEqual(False, response.json()['status'])
        
    def test_principal_registration_success(self):
        """
        Test to verify login success
        """
        data = {
            "email":"principal@gmail.com",
            "phone_number":"0000000000",
            "address":"US",
            "user_type":"principal",
            "password":"12345"
        }
        
        response = self.client.post(path=reverse("registration"), data=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['code'])
        self.assertEqual(True, response.json()['status'])
        
    def test_principal_registration_failed(self):
        """
        Test to verify login success
        """
        data = {
            "email":"principal@gmail.com",
            "phone_number":"0000000000",
            "address":"US",
        }
        
        response = self.client.post(path=reverse("registration"), data=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(400, response.json()['code'])
        self.assertEqual(False, response.json()['status'])
        
    def test_teacher_registration_success(self):
        """
        Test to verify login success
        """
        data = {
            "email":"teacher@gmail.com",
            "phone_number":"0000000000",
            "address":"US",
            "user_type":"teacher",
            "password":"12345",
            "qualification":"B.Tech",
            "year_of_experience":"3 years"
        }
        
        response = self.client.post(path=reverse("registration"), data=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['code'])
        self.assertEqual(True, response.json()['status'])
        
    def test_teacher_registration_failed(self):
        """
        Test to verify login success
        """
        data = {
            "email":"teacher@gmail.com",
            "phone_number":"0000000000",
            "address":"US",
            "password":"12345",
        }
        
        response = self.client.post(path=reverse("registration"), data=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(400, response.json()['code'])
        self.assertEqual(False, response.json()['status'])
        
    def test_student_registration_success(self):
        """
        Test to verify login success
        """
        data = {
            "email":"student@gmail.com",
            "phone_number":"000000000",
            "address":"US",
            "user_type":"student",
            "password":"12345",
            "bio":"test"
        }
        
        response = self.client.post(path=reverse("registration"), data=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()['code'])
        self.assertEqual(True, response.json()['status'])
        
    def test_student_registration_failed(self):
        """
        Test to verify login success
        """
        data = {
            "phone_number":"000000000",
            "address":"US",
            "user_type":"student",
        }
        
        response = self.client.post(path=reverse("registration"), data=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(400, response.json()['code'])
        self.assertEqual(False, response.json()['status'])
        
        
    

        