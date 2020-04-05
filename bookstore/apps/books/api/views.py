from rest_framework import viewsets
from ..models import Book
from .serializers import BooksSerializers


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializers
