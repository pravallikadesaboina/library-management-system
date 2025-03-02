import requests
from rest_framework import serializers
from .models import LibraryRecord

# Fetch student names from student_service API
def get_student_choices():
    try:
        response = requests.get("http://localhost:8001/student/")
        if response.status_code == 200:
            return [(student["name"], student["name"]) for student in response.json()]
    except:
        return []
    return []

# Fetch book names from book_service API
def get_book_choices():
    try:
        response = requests.get("http://localhost:8002/book/")
        if response.status_code == 200:
            return [(book["name"], book["name"]) for book in response.json()]
    except:
        return []
    return []

class LibraryRecordSerializer(serializers.ModelSerializer):
    student = serializers.ChoiceField(choices=get_student_choices())  # Dropdown for students
    book = serializers.ChoiceField(choices=get_book_choices())  # Dropdown for books

    class Meta:
        model = LibraryRecord
        fields = '__all__'

    def validate_student(self, value):
        """ Validate if the selected student exists in the student_service API """
        valid_students = dict(get_student_choices()).keys()
        if value not in valid_students:
            raise serializers.ValidationError("Selected student does not exist.")
        return value

    def validate_book(self, value):
        """ Validate if the selected book exists in the book_service API """
        valid_books = dict(get_book_choices()).keys()
        if value not in valid_books:
            raise serializers.ValidationError("Selected book does not exist.")
        return value

    def validate(self, data):
        """ Validate start and end dates """
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError({"end_date": "End date must be after start date."})

        return data
