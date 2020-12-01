import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class MyUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)


class Currency(models.Model):
    CCY_USD = 1
    CCY_EUR = 2
    CCY_RUR = 3

    CCY_CHOICES = (
        (CCY_USD, 'USD'),
        (CCY_EUR, 'EUR'),
        (CCY_RUR, 'RUR')
    )

    ccy = models.PositiveSmallIntegerField(choices=CCY_CHOICES)
    buy_price = models.DecimalField(max_digits=5, decimal_places=2)
    sell_price = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def convert_str_to_choice(cls, choice_name):
        choices = dict(map(reversed, cls.CCY_CHOICES))
        if choice_name in choices:
            return choices[choice_name]


class Logger(models.Model):
    time_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    request_path = models.CharField(max_length=255, null=True)
    request_method = models.CharField(max_length=255, null=True)
    execution_time = models.FloatField(null=True)

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        return self.request_path


class Student(models.Model):
    phone = models.CharField(max_length=255, verbose_name="Телефон", null=True)
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", null=True)
    age = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название группы")
    students = models.ManyToManyField("core.Student", blank=True)
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name


def send_notify(instance, **kwargs):
    from core.utils import notify
    notify(instance)


pre_save.connect(send_notify, sender=Student)
pre_save.connect(send_notify, sender=MyUser)
