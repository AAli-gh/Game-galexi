from django.urls import path
from rest_framework import routers
from django.urls import include, path
from .views import *
router = routers.DefaultRouter()

router.register(r'Creatuser', Creatuser,basename='Creatuser')


urlpatterns = [
    path('', include(router.urls)),


]
