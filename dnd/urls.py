from django.urls import path, include

from . import views

app_name = 'dnd'

urlpatterns = [
    path('npcs/', views.NPC, name='npcs'),
    path('npcs/<int:pk>/', views.detail, name='detail'),


]