from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


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
    age = models.PositiveIntegerField(null=True, validators=[MinValueValidator(9)])
    locations = models.ManyToManyField(default='Unknown',
                                       to='ads.Location'
                                       )
    # doesn't have an input_formats input_formats=settings.DATE_INPUT_FORMATS
    birth_date = models.DateField(null=True)

    # SELECT (1) AS "a" FROM "users_user" WHERE "users_user"."email" = ''
    email = models.EmailField(blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ("id",)

    # def __str__(self):
    #     return f'id={self.pk}.{self.first_name}'
