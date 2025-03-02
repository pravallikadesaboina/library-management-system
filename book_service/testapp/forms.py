from django import forms
from .models import Book
from datetime import datetime

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publication', 'year']
        widgets = {
            'year': forms.Select(choices=[(y, y) for y in range(datetime.now().year, datetime.now().year - 100, -1)]),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Book name must contain only letters and spaces.")
        return name

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author.replace(" ", "").isalpha():
            raise forms.ValidationError("Author name must contain only letters and spaces.")
        return author

    def clean_publication(self):
        publication = self.cleaned_data.get('publication')
        if len(publication) < 3:
            raise forms.ValidationError("Publication name must have at least 3 characters.")
        return publication

    def clean_year(self):
        year = int(self.cleaned_data.get('year'))
        current_year = datetime.now().year
        if year > current_year or year < current_year - 100:
            raise forms.ValidationError(f"Year must be between {current_year - 100} and {current_year}.")
        return year
