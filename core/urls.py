from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('browse/', include('browse.urls')),
    path('commission/', views.commission, name='commission'),
    path('menu/', views.menu_items, name='menu'),
    path('roll/',views.roll, name='roll'),
]