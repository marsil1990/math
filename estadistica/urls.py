from django.urls import path
from . import views
urlpatterns = [
    path('', views.est, name='est')
]
