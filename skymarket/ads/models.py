from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.db import models

from ads.Validators import check_positive
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=120)
    # TODO Не совсем понял зачем нужно было добавлять, логично было исправить name
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)], null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'id={self.pk}.{self.name}'


class Location(models.Model):
    name = models.CharField(max_length=70)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Координата'
        verbose_name_plural = 'Координаты'

    def __str__(self):
        return f'id={self.pk}.{self.name}'


class Ad(models.Model):
    STATUS = [
        ("TRUE", "В наличии"),
        ("FALSE", "Недоступна"),
    ]
    name = models.CharField(max_length=100, validators=[MinLengthValidator(10)], null=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, null=True, blank=True
    )
    # TODO да вроде бы у меня оно и так PositiveIntegerField
    price = models.PositiveIntegerField(null=True, blank=True, validators=[check_positive])
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='images/')
    is_published = models.CharField(max_length=13, default=False, choices=STATUS)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    #     # ordering = ("-price",)
    #
    # def __str__(self):
    #     return f'id={self.pk}.{self.name}.{self.price}'


class Selection(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True, blank=True
    )
    items = models.ManyToManyField(Ad, default='Unknown')


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True, blank=True
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
