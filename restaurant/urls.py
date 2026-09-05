from django.urls import path
from . import views

#define URL route for index() view
urlpatterns = [
    path('', views.index, name='index')
]
