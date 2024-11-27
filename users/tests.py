from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тесты для модели User"""

    def setUp(self):
        self.user = User.objects.create(email='test@example.com', first_name='Test', is_active=True)
        self.user.set_password('123qwe456')
        self.user.tg_nick = '@test_user'
        self.user.save()

    def test_create_user(self):
        """Тест регистрации нового пользователя"""
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('users:register'),
                                    {'email': 'test1@example.com',
                                     'first_name': 'Test1',
                                     'password': '123qwe456',
                                     'tg_nick': '@test_user'}
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_list(self):
        """Тест попытки доступа к списку пользователей"""
        self.client.force_authenticate(user=self.user)
        url = reverse('users:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_detail(self):
        """Тест получения информации о пользователе"""
        self.client.force_authenticate(user=self.user)
        url = reverse('users:detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_user_update(self):
        """Тест обновления информации о пользователе"""
        self.client.force_authenticate(user=self.user)
        url = reverse('users:update', kwargs={'pk': self.user.pk})
        response = self.client.patch(url, {'first_name': 'Test2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Test2')

    def test_user_delete(self):
        """Тест удаления пользователя"""
        self.client.force_authenticate(user=self.user)
        url = reverse('users:delete', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

    def test_jwt_token_serializer_valid(self):
        """Тест для сериализатора токена с валидными данными"""
        data = {'email': 'test@example.com', 'password': '123qwe456'}
        response = self.client.post('/users/login/', data)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_jwt_token_serializer_invalid(self):
        """Тест для сериализатора токена с невалидными данными"""
        data = {'email': 'test@example.com', 'password': 'wrong_password'}
        response = self.client.post('/users/login/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
