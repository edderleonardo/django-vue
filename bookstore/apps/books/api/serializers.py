from rest_framework import serializers
from ..models import Book


class BooksSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
        )
