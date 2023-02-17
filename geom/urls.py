from django.urls import path
from . import views

urlpatterns = [
    path('', views.geom, name ='geom' )
]