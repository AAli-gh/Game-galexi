from rest_framework import viewsets
from .models import *
from .serializers import *



class Creatuser(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer