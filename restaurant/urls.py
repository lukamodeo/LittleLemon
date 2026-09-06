from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, msg, MenuItemsView, SingleMenuItemView

#define URL route for index() view

urlpatterns = [
    path('', index, name='index'),
    path('menu-items', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token),
]

