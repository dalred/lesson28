# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path
from rest_framework import routers

from ads import views
from ads.views import LocationViewSet, CatViewSet

urlpatterns = [
    path('', views.root),
    path('ads/<int:pk>/', views.AdvRetrieveView.as_view()),
    path('ads/<int:pk>/upload_image/', views.AdvUpdateImageView.as_view()),
    path('ads/<int:pk>/delete/', views.AdvDeleteView.as_view()),
    path('ads/', views.ADVListViewSet.as_view()),
    path('ads/me/', views.AdvMeAPIView.as_view()),
    path('ads/create/', views.ADVCreateViewSet.as_view()),
    path('ads/<int:pk>/update/', views.ADVUpdateViewSet.as_view()),
    path('selections/', views.SelectionListViewAPI.as_view()),
    path('selections/<int:pk>/', views.SelectionRetrieveViewAPI.as_view()),
    path('selection/create/', views.SelectionCreateAPIView.as_view()),
    path('selection/<int:pk>/update/', views.SelectionUpdateAPIView.as_view()),
    path('selection/<int:pk>/delete/', views.SelectionDeleteAPIView.as_view()),
    path('ads/<int:pk>/comments/', views.AdCommentsListViewAPI.as_view()),
    path('ads/<int:pk>/comments/<int:commentId>/', views.AdCommentsRetrieveViewAPI.as_view()),
    path('comments/<int:pk>/', views.CommentRetrieveViewAPI.as_view()),
    path('comments/create/', views.CommentCreateAPIView.as_view()),
    path('comments/<int:pk>/update/', views.CommentUpdateAPIView.as_view()),
    path('comments/<int:pk>/delete/', views.CommentDeleteAPIView.as_view()),
]

router = routers.SimpleRouter()
router.register('locations', LocationViewSet)
router.register('cat', CatViewSet)
urlpatterns += router.urls

