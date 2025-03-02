from django.contrib import admin
from .models import LibraryRecord
import requests

class LibraryRecordAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'get_book_name', 'start_date', 'end_date')

    def get_student_name(self, obj):
        try:
            response = requests.get(f"http://localhost:8001/students/{obj.student}/")
            if response.status_code == 200:
                return response.json().get("name", "Unknown")
        except:
            return "Unknown"
    get_student_name.short_description = 'Student Name'

    def get_book_name(self, obj):
        try:
            response = requests.get(f"http://localhost:8002/books/{obj.book}/")
            if response.status_code == 200:
                return response.json().get("name", "Unknown")
        except:
            return "Unknown"
    get_book_name.short_description = 'Book Name'

admin.site.register(LibraryRecord, LibraryRecordAdmin)
