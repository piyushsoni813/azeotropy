from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='register_student'),
    path('success/', views.registration_success, name='registration_success'),
]