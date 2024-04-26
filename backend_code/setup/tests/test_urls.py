from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from setup.models import EducationalLevel
from setup.serializers import EducationalLevelSerializer
from django.contrib.auth.models import User


class EducationalLevelOpTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user and obtain the token
        self.user = User.objects.create_user(username='testuser', password='testuser')
        login_url = reverse('login')
        login_data = {'username': 'testuser', 'password': 'testuser'}
        response = self.client.post(login_url, data=login_data, format='json')
        self.token = response.data['token']
        # Authenticate the client with the token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_educational_level_op_add(self):
        url = reverse('EducationalLevelOp_add')
        data = {'name': 'Test Educational Level'}
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EducationalLevel.objects.count(), 1)
        self.assertEqual(EducationalLevel.objects.get().name, 'Test Educational Level')

    def test_educational_level_op_edit(self):
        educational_level = EducationalLevel.objects.create(name='Test Educational Level')
        url = reverse('EducationalLevelOp_edit', kwargs={'pk': educational_level.pk})
        data = {'name': 'Updated Educational Level'}
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(EducationalLevel.objects.get(pk=educational_level.pk).name, 'Updated Educational Level')

    def test_educational_level_op_delete(self):
        educational_level = EducationalLevel.objects.create(name='Test Educational Level')
        url = reverse('EducationalLevelOp_delete', kwargs={'pk': educational_level.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(EducationalLevel.objects.count(), 0)

    def test_get_educational_level_by_id(self):
        educational_level = EducationalLevel.objects.create(name='Test Educational Level')
        url = reverse('GetEducationalLevelById', kwargs={'pk': educational_level.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = EducationalLevelSerializer(educational_level)
        self.assertEqual(response.data['data'], serializer.data)

    def test_get_educational_level_list(self):
        EducationalLevel.objects.create(name='Test Educational Level 1')
        EducationalLevel.objects.create(name='Test Educational Level 2')
        url = reverse('GetEducationalLevelList')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 2)

    def test_educational_level_list_pagination(self):
        EducationalLevel.objects.create(name='Educational Level 1')
        EducationalLevel.objects.create(name='Educational Level 2')
        EducationalLevel.objects.create(name='Educational Level 3')
        EducationalLevel.objects.create(name='Educational Level 4')
        EducationalLevel.objects.create(name='Educational Level 5')
        # Define the pagination payload
        payload = {
            "pageNum": 2,
            "pageLen": 2
        }
        # Send a POST request to the endpoint with the pagination payload
        url = reverse('EducationalLevelList')
        response = self.client.post(url, data=payload, format='json')

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response contains the correct number of items per page
        expected_items_per_page = 2
        response_data = response.data
        self.assertEqual(len(response_data['data']), expected_items_per_page)

        # Assert that the response contains the correct total count of items
        total_items_count = EducationalLevel.objects.count()
        self.assertEqual(response_data['count'], total_items_count)

        # Assert that the response data matches the serialized data of the expected objects
        serializer = EducationalLevelSerializer(
            EducationalLevel.objects.all().order_by('id')[expected_items_per_page:expected_items_per_page * 2],
            many=True
        )
        self.assertEqual(response_data['data'], serializer.data)

