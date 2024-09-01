from rest_framework import viewsets
from rest_framework.response import Response
from .models import Expert, RetiredExpert
from .serializers import ExpertSerializer, RetiredExpertSerializer

class ExpertViewSet(viewsets.ModelViewSet):
    queryset = Expert.objects.filter(is_active=True)
    serializer_class = ExpertSerializer

class RetiredExpertViewSet(viewsets.ModelViewSet):
    queryset = RetiredExpert.objects.all()
    serializer_class = RetiredExpertSerializer