from django import forms
from .models import Book, Student


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "isbn": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "total_copies": forms.NumberInput(attrs={"class": "form-control"}),
            "available_copies": forms.NumberInput(attrs={"class": "form-control"}),
            "published_year": forms.NumberInput(attrs={"class": "form-control"}),
        }


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "department": forms.TextInput(attrs={"class": "form-control"}),
        }