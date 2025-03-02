from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import LibraryRecord
from .serializers import LibraryRecordSerializer
# Library APIs
class LibraryRecordListCreateView(generics.ListCreateAPIView):
    queryset = LibraryRecord.objects.all()
    serializer_class = LibraryRecordSerializer

class LibraryRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryRecord.objects.all()
    serializer_class = LibraryRecordSerializer
