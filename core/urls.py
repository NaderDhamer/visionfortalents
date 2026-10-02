from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('training/', views.training, name='training'),
    path('work-packages/<slug:slug>/', views.work_package_detail, name='work_package_detail'),
    path('sab-members/', views.sab_members, name='sab_members'),
    path('consortium/', views.consortium, name='consortium'),
    path('contact/', views.contact, name='contact'),
]