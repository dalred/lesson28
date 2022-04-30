from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    member = "member"
    moderator = "moderator"
    admin = "admin"
    ROLE = [
        (member, 'пользователь'),
        (moderator, 'moderator'),
        (admin, 'admin')
    ]

    first_name = models.CharField(max_length=20, default='Unknown')
    last_name = models.CharField(max_length=20, default='Unknown')
    role = models.CharField(max_length=10, default='Unknown', choices=ROLE, null=True)
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField(default='Unknown',
                                       to='ads.Location'
                                       )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ("id",)

    def __str__(self):
        return f'id={self.pk}.{self.first_name}'
