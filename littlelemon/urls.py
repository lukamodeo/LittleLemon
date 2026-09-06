"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import UserViewSet, BookingViewSet


# Router for users at root
user_router = DefaultRouter()
user_router.register(r'users', UserViewSet)

# Router for tables under restaurant/booking/
booking_router = DefaultRouter()
booking_router.register(r'tables', BookingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    # users at root
    path('', include(user_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # tables under restaurant/booking/
    path('restaurant/booking/', include(booking_router.urls)),
]