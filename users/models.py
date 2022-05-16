from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserManager(BaseUserManager):
    """
    функция создания пользователя — в нее мы передаем обязательные поля
    """

    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role="user"
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """
        функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password
        )

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user = "user"
    moderator = "moderator"
    admin = "admin"
    ROLE = [
        (user, 'пользователь'),
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
    phone = models.CharField(max_length=20, default='Unknown')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ("id",)

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'
    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role", "birth_date"]

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == self.admin

    @property
    def is_user(self):
        return self.role == self.user
