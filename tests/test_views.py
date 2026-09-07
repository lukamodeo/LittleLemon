from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create token for the user
        token = Token.objects.create(user=self.user)
        print(f"TOKEN ==> {token.key}")
        # Authenticate client with token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        # Create items for test
        MenuItem.objects.create(title="Pizza", price=150, inventory=50)
        MenuItem.objects.create(title="Burger", price=100, inventory=30)

    def test_getall(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)