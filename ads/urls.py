# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from ads import views
from ads.views import LocationViewSet, CatViewSet

urlpatterns = [
    path('', views.root),
    path('ad/<int:pk>', views.AdvRetrieveView.as_view()),
    path('ad/<int:pk>/update/', views.AdvUpdateView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdvUpdateImageView.as_view()),
    path('ad/<int:pk>/delete/', views.AdvDeleteView.as_view()),
    path('user/', views.AuthorListAPIView.as_view()),
    path('user/published/<int:pk>', views.AuthorPublishedAPIView.as_view()),
    path('user/<int:pk>', views.AuthorRetrieveView.as_view()),
    path('user/create/', views.AuthorCreateView.as_view()),
    path('user/<int:pk>/delete/', views.AuthorDeleteView.as_view()),
    path('user/<int:pk>/update/', views.AuthorUpdateView.as_view()),
    path('ad/', views.ADVListViewSet.as_view()),
    path('ad/create/', views.ADVCreateViewSet.as_view())
]


router = routers.SimpleRouter()
router.register('locations', LocationViewSet)
router.register('cat', CatViewSet)

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
