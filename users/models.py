from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name=_('Email'))
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_('Аватар'), )
    phone_number = models.CharField(max_length=15, blank=True, verbose_name=_('Номер телефона'), )
    country = models.CharField(max_length=50, blank=True, verbose_name=_('Страна'))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    token = models.CharField(max_length=255, verbose_name=_('Токен'), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email