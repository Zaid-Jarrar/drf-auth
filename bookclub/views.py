from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Bookclub
from .serializers import BookclubSerializer
# Create your views here.


class BooksListView(ListCreateAPIView):
    queryset = Bookclub.objects.all()
    serializer_class = BookclubSerializer
    permission_classes = (IsAuthenticated,)


class BooksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bookclub.objects.all()
    serializer_class = BookclubSerializer
    permission_classes = (IsAuthenticated,)