from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
]
