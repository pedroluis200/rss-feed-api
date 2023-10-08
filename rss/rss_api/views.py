from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import RSSFeed, SelectedFeed
from .serializers import RSSFeedSerializer, SelectedFeedSerializer

# Vista para listar y crear feeds RSS
class RSSFeedListCreateView(generics.ListCreateAPIView):
    queryset = RSSFeed.objects.all()
    serializer_class = RSSFeedSerializer

# Vista para ver, actualizar y eliminar feeds RSS por ID
class RSSFeedDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RSSFeed.objects.all()
    serializer_class = RSSFeedSerializer

# Vista para listar y crear feeds seleccionados
class SelectedFeedListCreateView(generics.ListCreateAPIView):
    queryset = SelectedFeed.objects.all()
    serializer_class = SelectedFeedSerializer

# Vista para ver, actualizar y eliminar feeds seleccionados por ID
class SelectedFeedDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SelectedFeed.objects.all()
    serializer_class = SelectedFeedSerializer