from django.urls import path

from . import views



app_name = 'browse'

urlpatterns = [
    path('', views.index, name='index'),
    path('shangri-la/',views.garden,name='shangri-la')
    #path('', views.index, name='about'),
]