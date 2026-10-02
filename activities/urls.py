from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.index, name='index'),
    path('benchmarking/', views.benchmarking, name='benchmarking'),
    path('media/', views.media, name='media'),
    path('events/', views.events, name='events'),
]