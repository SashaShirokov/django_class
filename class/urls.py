from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='class-home'),
    path('about/', views.about, name='class-about'),
]
