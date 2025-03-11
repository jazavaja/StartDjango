from datetime import datetime, date

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from modellearn.models import Person
from myapi.models import ProductApi


# Create your tests here.

class TestTokenAuthApi(TestCase):
    def setUp(self) -> None:
        self.user = Person.objects.create(username='test_user', password='test_user')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

    def test_person_get(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.client.get('/api/test_api')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestJWTAuthApi(TestCase):
    def setUp(self):
        self.user = Person.objects.create_user(
            username='testtest',
            password='testtest',
            is_active=True
        )
        self.client = APIClient()

        response = self.client.post('/api/jwt_create', {
            'username': 'testtest',
            'password': 'testtest',
        })
        self.token = response.data['access']

    def test_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get('/api/test_api')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUpdateDeleteUser(TestCase):
    def setUp(self) -> None:
        self.product = ProductApi.objects.create(
            name='pp',
            description='oo',
            price=19,
            create_at=datetime.now()
        )
        self.client = APIClient()

    def test_update(self):
        data = {
            'description': 'test_update',
            'price': 10000,
            'name': 'updated_name',
            'create_at': date.today()
        }
        url = reverse('class_list_products', args=[self.product.id])
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code,status.HTTP_200_OK)

        # self.assertEqual(response.data['username'],'test_update')

    # def test_delete(self):
    #     response = self.client.delete(f'/api/class_view_product_update_view/{self.product.id}/', format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     with self.assertRaises(ProductApi.DoesNotExist):
    #         ProductApi.objects.get(self.product.id)
    #
    #     pass
