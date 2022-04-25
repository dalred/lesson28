from django.db import models


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


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(
        Location
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ("username",)

    def __str__(self):
        return f'id={self.pk}.{self.first_name}'


class Ad(models.Model):
    STATUS = [
        ("TRUE", "В наличии"),
        ("FALSE", "Недоступна"),
    ]
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, null=True
    )
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='images/')
    is_published = models.CharField(max_length=13, default=True, choices=STATUS)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        # ordering = ("-price",)

    def __str__(self):
        return f'id={self.pk}.{self.name}'
