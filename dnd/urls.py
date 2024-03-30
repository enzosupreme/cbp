from django.urls import path, include

from . import views

app_name = 'dnd'

urlpatterns = [
    path('npcs/', views.NPC, name='npcs'),
    path('characters/', views.Character, name='characters'),
    path('new/', views.new, name='new'),
    path('npcs/<int:pk>/', views.detail, name='detail'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),


]