from django.urls import path, include

from . import views

app_name = 'terrarium'

urlpatterns = [
    path('terrarium/', views.terrariums, name='terrariums'),
    path('terrarium/<int:pk>/', views.detail, name='detail'),
    path('plant/<int:pk>/', views.plant_detail, name='plant'),
    path('plants/',views.plants, name='plants')

]