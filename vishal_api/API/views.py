from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LanguagesSerializer, DevelopersSerializer
from .models import Languages,Developers


class LanguagesView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer


class DevelopersView(viewsets.ModelViewSet):
    queryset = Developers.objects.all()
    serializer_class = DevelopersSerializer


