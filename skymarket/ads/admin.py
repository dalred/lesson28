from django.contrib import admin

from ads.models import Ad, Location, Category
from users.models import User

admin.site.register(Ad)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Category)