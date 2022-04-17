from django.contrib import admin

from ads.models import Ad, Author, Location, Category

admin.site.register(Ad)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Category)