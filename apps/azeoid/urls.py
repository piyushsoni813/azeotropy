from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'azeoid'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('verify/', views.verify_azeoid, name='verify'),
    path('login/', auth_views.LoginView.as_view(template_name='azeoid/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
