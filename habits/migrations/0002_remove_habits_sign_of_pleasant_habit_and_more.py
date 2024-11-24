# Generated by Django 5.1.3 on 2024-11-23 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habits',
            name='sign_of_pleasant_habit',
        ),
        migrations.AlterField(
            model_name='habits',
            name='complete_time',
            field=models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='Время на выполнение привычки'),
        ),
        migrations.AlterField(
            model_name='habits',
            name='frequency',
            field=models.PositiveSmallIntegerField(default=1, help_text='укажите периодичность выполнения привычки в днях (по умолчанию ежедневная)', verbose_name='периодичность привычки, в днях'),
        ),
        migrations.AlterField(
            model_name='habits',
            name='place',
            field=models.CharField(blank=True, help_text='место, в котором выполняется привычка', max_length=100, null=True, verbose_name='место'),
        ),
    ]