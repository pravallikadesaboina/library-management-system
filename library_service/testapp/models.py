from django.db import models


# Create your models here.
class LibraryRecord(models.Model):
    student = models.CharField(max_length=255)  # Store student name as string
    book = models.CharField(max_length=255)  # Store book name as strin
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.book.name}"