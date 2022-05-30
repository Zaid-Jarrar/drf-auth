from rest_framework import serializers
from .models import Bookclub

class BookclubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookclub
        fields = ('id', 'title', 'author', 'description', 'rating', 'created_at', 'updated_at')