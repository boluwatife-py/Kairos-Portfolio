from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("secure-audio/<str:filename>/", views.secure_audio_stream, name="secure_audio_stream"),
]