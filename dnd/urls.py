from django.urls import path, include

from . import views

app_name = 'dnd'

urlpatterns = [
    path('npcs/', views.NPC, name='npcs'),
    path('characters/', views.Character, name='characters'),
    path('spell_list/', views.spell_list, name='spells'),
    path('npcs/<int:pk>/', views.detail, name='detail'),
    path('dm/', views.dm_items, name='dm_items'),
    path('monsters/', views.monster, name='monsters'),
    path('maps/', views.maps, name='maps'),
    path('area/<int:pk>/', views.area, name='areas'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
    path('spells/<int:pk>/', views.spell_description, name='spell_description'),
    path('special_items/', views.special_items_list, name='items'),
    path('item/<int:pk>/', views.special_items, name='special_items'),
    path('shop/<int:pk>/', views.shopper, name='shoppers'),
    path('characters/<int:pk>/edit/', views.character_edit, name='edit'),
    path('shops/',views.special_shops, name='shops'),


]