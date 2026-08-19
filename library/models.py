from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)

    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    published_year = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IssueTransaction(models.Model):

    STATUS_CHOICES = [
        ('ISSUED', 'Issued'),
        ('RETURNED', 'Returned'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    return_date = models.DateField(null=True, blank=True)

    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ISSUED'
    )

    def __str__(self):
        return f"{self.student.name} - {self.book.title}"