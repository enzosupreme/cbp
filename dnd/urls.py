from django.urls import path, include

from . import views

app_name = 'dnd'

urlpatterns = [
    path('npcs/', views.NPC, name='npcs'),
    path('characters/', views.Character, name='characters'),
    path('spell_list/', views.spell_list, name='spells'),
    path('new/', views.new, name='new'),
    path('npcs/<int:pk>/', views.detail, name='detail'),
    path('dm/', views.dm_items, name='dm_items'),
    path('monsters/', views.monster, name='monsters'),
    path('maps/', views.maps, name='maps'),
    path('area/<int:pk>/', views.area, name='areas'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
    path('spells/<int:pk>/', views.spell_description, name='spell_description'),


]