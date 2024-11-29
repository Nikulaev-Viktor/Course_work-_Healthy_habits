import logging

from celery import shared_task
from habits.services import send_telegram_message
from django.conf import settings
import pytz
from datetime import datetime, timedelta
from habits.models import Habits

logger = logging.getLogger(__name__)


@shared_task()
def telegram_notification():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_time = datetime.now(zone)
    current_time_less = current_time - timedelta(minutes=5)

    habits = Habits.objects.filter(
        time__lte=current_time.time(),
        time__gte=current_time_less.time()
    ).select_related('user')

    logger.info(f'Found {habits.count()} habits to notify')

    for habit in habits:
        user_tg = habit.user.tg_chat_id
        message = f'я буду {habit.action} в {habit.time} : {habit.place}'

        if user_tg:
            try:
                send_telegram_message(user_tg, message)
                logger.info(f'Отправлено сообщение {user_tg}: {message}')
            except Exception as e:
                logger.error(f'Ошибка при отправке сообщения {user_tg}: {e}')
        else:
            logger.warning(f'Не найден chat_id для пользователя: {habit.user}')
