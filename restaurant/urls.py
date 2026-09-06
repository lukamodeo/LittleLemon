from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView

#define URL route for index() view

urlpatterns = [
    path('', index, name='index'),
    path('menu/items', MenuItemsView.as_view()),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view()),
]

