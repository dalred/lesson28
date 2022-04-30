# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import users.views

urlpatterns = [
    path('users/', users.views.AuthorListAPIView.as_view()),
    path('user/published/<int:pk>', users.views.AuthorPublishedAPIView.as_view()),
    path('user/<int:pk>/', users.views.AuthorRetrieveView.as_view()),
    path('user/<int:pk>/delete/', users.views.AuthorDeleteView.as_view()),
    path('user/<int:pk>/update/', users.views.AuthorUpdateView.as_view()),
    path('register/', users.views.AuthorCreateView.as_view()),
    path('login/', views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]