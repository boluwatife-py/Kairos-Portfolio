from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('forms/contact/', views.contact_ajax, name='contact_ajax'),
]