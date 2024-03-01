from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        self.menu1 = Menu.objects.create(title='Menu 1', price=10.99, inventory=10)
        self.menu2 = Menu.objects.create(title='Menu 2', price=15.99, inventory=5)

    def test_getall(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
