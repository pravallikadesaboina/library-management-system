import requests
from django import forms
from .models import LibraryRecord
from datetime import datetime

class LibraryRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LibraryRecordForm, self).__init__(*args, **kwargs)

        # Fetch student names from student_service API
        try:
            response = requests.get("http://localhost:8001/student/")
            if response.status_code == 200:
                students = [(student["name"], student["name"]) for student in response.json()]
            else:
                students = []
        except:
            students = []
        self.fields['student'].choices = [('', 'Select Student')] + students

        # Fetch book names from book_service API
        try:
            response = requests.get("http://localhost:8002/book/")
            if response.status_code == 200:
                books = [(book["name"], book["name"]) for book in response.json()]
            else:
                books = []
        except:
            books = []
        self.fields['book'].choices = [('', 'Select Book')] + books

    student = forms.ChoiceField(choices=[], required=True)
    book = forms.ChoiceField(choices=[], required=True)

    class Meta:
        model = LibraryRecord
        fields = ['student', 'book', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_student(self):
        """ Validate if the selected student exists in the API response """
        student = self.cleaned_data.get('student')
        response = requests.get("http://localhost:8001/student/")
        if response.status_code == 200:
            student_names = [student["name"] for student in response.json()]
            if student not in student_names:
                raise forms.ValidationError("Selected student does not exist.")
        else:
            raise forms.ValidationError("Failed to fetch student list.")
        return student

    def clean_book(self):
        """ Validate if the selected book exists in the API response """
        book = self.cleaned_data.get('book')
        response = requests.get("http://localhost:8002/book/")
        if response.status_code == 200:
            book_names = [book["name"] for book in response.json()]
            if book not in book_names:
                raise forms.ValidationError("Selected book does not exist.")
        else:
            raise forms.ValidationError("Failed to fetch book list.")
        return book

    def clean(self):
        """ Validate start and end dates """
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("End date must be after start date.")
            if start_date < datetime.today().date():
                raise forms.ValidationError("Start date cannot be in the past.")

        return cleaned_data
