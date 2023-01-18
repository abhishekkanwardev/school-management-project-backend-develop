from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from accounts.models import User
from django.contrib.auth.models import Group
from school_process.models import Class

client = APIClient()


class ClassAPIViewTestCase(APITestCase):
    
    def setUp(self):
        self.email = "admin@gmail.com"
        self.password = "12345"
        
        self.user = User.objects.create_user(
            self.email, self.password
        )
        group = Group.objects.create(name='admin')
        self.user.groups.add(group)
        
        self.class_obj = Class.objects.create(class_name='11', class_description='11')
        
        
        
        self.access_token, self.refresh_token = self.user_login()
        
    def user_login(self):
        data = {
            "email": self.email,
            "password": self.password
        }
        
        response = self.client.post(path=reverse("token_obtain_pair"), data=data)
        access_token = response.json()['data']['access']
        refresh_token = response.json()['data']['refresh']
        return access_token, refresh_token
    
    def test_list_class_application_success(self):
        """
        Test to verify lis class success
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(path=reverse("admission_process:class-list"))
        self.assertEqual(200, response.status_code)
        
    def test_create_class_application_success(self):
        """
        Test to verify create class success
        """
        
        data = {
            "class_name": "10",
            "class_description": "10"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(path=reverse("admission_process:class-list"), data=data)
        self.assertEqual(201, response.status_code)
        
    def test_retrive_class_application_success(self):
        """
        Test to verify retrive class success
        """
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(path=reverse("admission_process:class-detail", kwargs={'pk': self.class_obj.id}))
        self.assertEqual(200, response.status_code)
        
    def test_update_class_application_success(self):
        """
        Test to verify update class success
        """
        data = {
            "class_name": "10",
            "class_description": "10 update"
        }
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.put(path=reverse("admission_process:class-detail", kwargs={'pk': self.class_obj.id}), data=data)
        self.assertEqual(200, response.status_code)
        
    def test_delete_class_application_success(self):
        """
        Test to verify delete class success
        """

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.delete(path=reverse("admission_process:class-detail", kwargs={'pk': self.class_obj.id}))
        self.assertEqual(204, response.status_code)
        
        
    
    # def test_create_admission_application_success(self):
    #     """
    #     Test to verify login success
    #     """
    #     data = {
    #         "student_first_name": "test",
    #         "student_last_name": "test",
    #         "health_insurance": "test",
    #         "date_of_birth": '2022-11-11',
    #         "gender": 'Male',
    #         "email": "test@gmail.com",
    #         "year_of_entry": '2022-11-11',
    #         "period": "2",
    #         "surname_doe": "test",
    #         "guardian_first_name": "test",
    #         "guardian_last_name": "test",
    #         "guardian_address": "test",
    #         "home_phone_no": "00000000",
    #         "guardian_mobile_no": "000000000",
    #         "previous_school_name": "test",
    #         "city": "US",
    #         "state": "US",
    #         "starting_date": '2022-11-11',
    #         "departure_date": '2022-11-11',
    #         "notes": "",
    #         "class_name": "1"
    #     }
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
    #     response = self.client.post(path=reverse("admission_process:admission-list"), data=data)
    #     self.assertEqual(200, response.status_code)
    #     self.assertEqual(200, response.json()['code'])
    #     self.assertEqual(True, response.json()['status'])
    