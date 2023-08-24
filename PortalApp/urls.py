
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('portal/', views.portal, name='portal'),
    path('signout/', views.signout, name='signout'),
]
