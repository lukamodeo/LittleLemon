from django.urls import path, include
from rest_framework import routers
from .views import index, MenuItemsView, SingleMenuItemView, UserViewSet

#define URL route for index() view

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('menu/items', MenuItemsView.as_view()),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view()),
    # Moved to project urls.py for project-level import
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Expose router.urls for project-level import
api_urls = router.urls