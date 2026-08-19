from django.urls import path
from . import views

urlpatterns = [
    
    # Dashboard
    path("", views.dashboard, name="dashboard"),

    # Books
    path("books/", views.home, name="home"),
    path("add/", views.add_book, name="add_book"),
    path("update/<int:id>/", views.update_book, name="update_book"),
    path("delete/<int:id>/", views.delete_book, name="delete_book"),

    # Students
    path("students/", views.students, name="students"),
    path("students/add/", views.add_student, name="add_student"),

    # Transactions
    path("issue/", views.issue_book, name="issue_book"),
    path("transactions/", views.transactions, name="transactions"),
    path("return/<int:id>/", views.return_book, name="return_book"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
]