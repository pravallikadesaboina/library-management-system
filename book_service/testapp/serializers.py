from rest_framework import serializers
from .models import Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    current_year = datetime.now().year
    YEAR_CHOICES = [(y, y) for y in range(current_year, current_year - 100, -1)]
    
    year = serializers.ChoiceField(choices=YEAR_CHOICES)  # Set dropdown choices here

    class Meta:
        model = Book
        fields = '__all__'
