from django.urls import path, include

from . import views

app_name = 'dnd'

urlpatterns = [
    path('npcs/', views.NPC, name='npcs'),
    path('characters/', views.Character, name='characters'),
    path('spell_list/', views.spell_list, name='spells'),
    path('shop1/', views.level_1_shop, name='shop1'),
    path('shop2/', views.level_2_shop, name='shop2'),
    path('shop3/', views.level_3_shop, name='shop3'),
    path('shop4/', views.level_4_shop, name='shop4'),
    path('shop5/', views.level_5_shop, name='shop5'),
    path('shop6/', views.level_6_shop, name='shop6'),
    path('new/', views.new, name='new'),
    path('npcs/<int:pk>/', views.detail, name='detail'),
    path('dm/', views.dm_items, name='dm_items'),
    path('monsters/', views.monster, name='monsters'),
    path('maps/', views.maps, name='maps'),
    path('area/<int:pk>/', views.area, name='areas'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
    path('spells/<int:pk>/', views.spell_description, name='spell_description'),
    path('special_items/', views.special_items_list, name='items'),
    path('item/<int:pk>/', views.special_items, name='special_items'),


]