from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.home, name='home'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
]
