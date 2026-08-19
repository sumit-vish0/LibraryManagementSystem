from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Book, Student, IssueTransaction
from .forms import BookForm, StudentForm


# ---------------- HOME ---------------- #
@login_required
def home(request):

    search = request.GET.get("search")

    if search:

        books = Book.objects.filter(
            title__icontains=search
        )

    else:

        books = Book.objects.all()

    return render(
        request,
        "library/home.html",
        {
            "books": books
        }
    )


# ---------------- BOOK CRUD ---------------- #
@login_required
def add_book(request):

    if request.method == "POST":

        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:

        form = BookForm()

    return render(request, "library/add_book.html", {"form": form})

@login_required
def update_book(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == "POST":

        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:

        form = BookForm(instance=book)

    return render(request, "library/add_book.html", {"form": form})

@login_required
def delete_book(request, id):

    book = get_object_or_404(Book, id=id)

    book.delete()

    return redirect("home")


# ---------------- STUDENT ---------------- #
@login_required
def students(request):

    students = Student.objects.all()

    return render(
        request,
        "library/student.html",
        {
            "students": students
        }
    )

@login_required
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("students")

    else:

        form = StudentForm()

    return render(
        request,
        "library/add_student.html",
        {
            "form": form
        }
    )


# ---------------- ISSUE BOOK ---------------- #
@login_required
def issue_book(request):

    books = Book.objects.all()
    students = Student.objects.all()

    if request.method == "POST":

        student = Student.objects.get(id=request.POST["student"])

        book = Book.objects.get(id=request.POST["book"])

        if book.available_copies <= 0:

            return render(
                request,
                "library/issue_book.html",
                {
                    "books": books,
                    "students": students,
                    "error": "Book not available"
                }
            )

        already_issued = IssueTransaction.objects.filter(
            student=student,
            book=book,
            status="ISSUED"
        ).exists()

        if already_issued:

            return render(
                request,
                "library/issue_book.html",
                {
                    "books": books,
                    "students": students,
                    "error": "Book already issued to this student"
                }
            )

        IssueTransaction.objects.create(

            student=student,

            book=book,

            due_date=timezone.now().date() + timedelta(days=14)

        )

        book.available_copies -= 1

        book.save()

        return redirect("transactions")

    return render(
        request,
        "library/issue_book.html",
        {
            "books": books,
            "students": students
        }
    )


# ---------------- RETURN BOOK ---------------- #
@login_required
def return_book(request, id):

    transaction = get_object_or_404(
        IssueTransaction,
        id=id
    )
    if transaction.status == "ISSUED":
        today = timezone.now().date()
        transaction.return_date = today
        transaction.status = "RETURNED"
        if today > transaction.due_date:
            late_days = (
                today - transaction.due_date
            ).days
            transaction.fine = late_days * 10
        transaction.save()
        book = transaction.book
        book.available_copies += 1
        book.save()
    return redirect("transactions")


# ---------------- TRANSACTIONS ---------------- #
@login_required
def transactions(request):

    transactions = IssueTransaction.objects.all().order_by("-issue_date")
    return render(
        request,
        "library/transactions.html",
        {
            "transactions": transactions
        }
    )

# ---------------- DASHBOARD ---------------- #
@login_required
def dashboard(request):

    total_books = Book.objects.count()
    total_students = Student.objects.count()
    issued_books = IssueTransaction.objects.filter(
        status="ISSUED"
    ).count()
    available_books = Book.objects.all()
    available = 0
    for book in available_books:
        available += book.available_copies
    return render(
        request,
        "library/dashboard.html",
        {
            "total_books": total_books,
            "total_students": total_students,
            "issued_books": issued_books,
            "available_books": available
        }
    )

def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user:

            login(request, user)

            return redirect("dashboard")

        else:

            return render(
                request,
                "library/login.html",
                {
                    "error": "Invalid Username or Password"
                }
            )

    return render(request, "library/login.html")


def logout_view(request):

    logout(request)

    return redirect("login")