from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from habits.models import Habits
from users.models import User
from django.test import TestCase


class HabitsTestCase(TestCase):
    """Тесты для модели Habits"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', first_name='Test', is_active=True)
        self.user.set_password('123qwe456')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.habit1 = Habits.objects.create(
            user=self.user,
            action='делать зарядку',
            time='07:00',
            place='дома',
            reward='прогулка',
            frequency=1,
            is_pleasant=True,
            complete_time='00:02:00',
            is_public=False,
        )
        self.habit2 = Habits.objects.create(
            user=self.user,
            action='пить воду',
            time='09:00',
            place='работа',
            reward='перерыв',
            frequency=2,
            is_pleasant=True,
            complete_time='00:01:30',
            is_public=False,
        )

    def tearDown(self):
        Habits.objects.all().delete()

    def test_list_habits(self):
        """Тест списка привычек"""
        url = reverse('habits:list')
        response = self.client.get(url)
        print(f"Response data: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_habit_detail(self):
        """Тест детализации привычки"""
        url = reverse("habits:detail", kwargs={"pk": self.habit1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        """Тест создания привычки"""
        url = reverse('habits:create')
        data = {
            'action': 'делать зарядку',
            'time': '07:00',
            'place': 'дома',
            'reward': 'прогулка',
            'frequency': 1,
            'is_pleasant': False,
            'complete_time': '00:02:00',
            'is_public': False,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.all().count(), 3)
        new_habit = Habits.objects.last()
        self.assertFalse(new_habit.is_pleasant)
        self.assertEqual(new_habit.user, self.user)
        self.assertEqual(new_habit.reward, 'прогулка')

    def test_habit_update(self):
        """Тест обновления привычки"""
        url = reverse('habits:update', kwargs={'pk': self.habit1.pk})
        data = {
            'action': 'делать зарядку',
            'time': '07:00',
            'place': 'на улице',
            'reward': 'прогулка',
            'frequency': 1,
            'is_pleasant': False,
            'complete_time': '00:02:00',
            'is_public': False,
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit1.refresh_from_db()
        self.assertEqual(self.habit1.place, "на улице")

    def test_habit_delete(self):
        """Тест удаления привычки"""
        url = reverse('habits:delete', kwargs={'pk': self.habit1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 1)

    def test_habit_public_list(self):
        """Тест списка публичных привычек"""
        url = reverse('habits:public_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
