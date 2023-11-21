from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm



app_name = 'browse'

urlpatterns = [
    path('', views.index, name='index'),
    path('shangri-la/',views.garden,name='shangri-la'),
    path('<int:pk>/', views.image, name='images'),
    path('thermo/',views.thermo, name='thermo'),
    path('santa/',views.santa, name='santas'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='browse/login.html',authentication_form=LoginForm), name='login'),
]