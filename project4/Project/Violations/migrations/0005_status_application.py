# Generated by Django 5.0.6 on 2024-05-22 17:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Violations', '0004_alter_role_options_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'Новое'), ('1', 'Подтверждено'), ('2', 'Отклонено')], max_length=10, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус заявки',
                'verbose_name_plural': 'Статус заявки',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=20, verbose_name='номер автомобиля')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('0', 'Новое'), ('1', 'Подтверждено'), ('2', 'Отклонено')], max_length=10)),
                ('date_of_submission', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='applications/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
