from rest_framework import routers
from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'developers', DeveloperViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'games', GameViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'userlibraries', UserLibraryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'userprofiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]