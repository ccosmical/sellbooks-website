from rest_framework.serializers import ModelSerializer
from .models import books


class booksSerializer(ModelSerializer):
    class Meta:
        model = books
        fields=('title', 'author', 'publication_date', 'ISBN', 'category')