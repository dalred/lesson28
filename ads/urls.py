# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from ads import views

urlpatterns = [
    path('', views.root),
    path('cat/', views.CategoryView.as_view()),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),
    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>', views.AdvDetailView.as_view()),
    path('ad/<int:pk>/update/', views.AdvUpdateView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdvUpdateImageView.as_view()),
    path('ad/<int:pk>/delete/', views.AdvDeleteView.as_view()),
    path('user/', views.AuthorView.as_view()),
    path('user/published/<int:pk>', views.AuthorPublishedView.as_view()),
    path('user/<int:pk>', views.AuthorDetailView.as_view()),
    path('user/create/', views.AuthorCreateView.as_view()),
    path('user/<int:pk>/delete/', views.AuthorDeleteView.as_view()),
    path('user/<int:pk>/update/', views.AuthorUpdateView.as_view()),
    path('locations/', views.LocationListView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
