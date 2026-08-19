from django.contrib import admin
from .models import Book, Student,IssueTransaction

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssueTransaction)