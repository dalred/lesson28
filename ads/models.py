from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'id={self.pk}.{self.name}'


class Location(models.Model):
    name = models.CharField(max_length=50)
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
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='images/')
    is_published = models.CharField(max_length=13, default=True, choices=STATUS)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    #     # ordering = ("-price",)
    #
    def __str__(self):
        return f'id={self.pk}.{self.name}'


class Selection(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True, blank=True
    )
    items = models.ManyToManyField(Ad, default='Unknown')
