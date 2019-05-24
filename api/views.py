from django.shortcuts import render

from rest_framework import generics

from songs.models import NewVideo

from .serializers import NewVideoSerializer

# Create your views here.

class NewVideoAPIView(generics.ListCreateAPIView):
	queryset = NewVideo.objects.all()
	serializer_class = NewVideoSerializer

