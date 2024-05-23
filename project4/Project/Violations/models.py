from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    telephone = models.CharField(max_length=15, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return '%s' % (self.username)


class Status(models.Model):
    STATUS_CHOICES = (
        ('0', 'Новое'),
        ('1', 'Подтверждено'),
        ('2', 'Отклонено')
    )

    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статус заявки'

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=20, verbose_name="Номер автомобиля")
    description = models.TextField(max_length=300, verbose_name='Описание')
    status = models.CharField(max_length=10, choices=Status.STATUS_CHOICES)
    date_of_submission = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='applications/', verbose_name='Изображения')

    def __str__(self):
        return f'{self.user.username} - {self.car_number}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
