# Library Management System

A web-based **Library Management System** built with **Python and Django**. The application helps manage books, students, book issuing and returning, transactions, and library records through a simple dashboard.

## Features

* 🔐 User login and logout
* 📊 Library dashboard
* 📚 Add, update, delete, and search books
* 👨‍🎓 Add and manage students
* 📖 Issue books to students
* 🔄 Return issued books
* 💰 Automatic fine calculation for late returns
* 📋 View book issue and return transactions
* 🎨 Responsive interface with custom CSS
* 🗄️ MySQL database support

## Technologies Used

* **Python**
* **Django**
* **MySQL**
* **HTML5**
* **CSS3**
* **Django Templates**

## Project Structure

```text
LibraryManagement/
│
├── library/
│   ├── migrations/
│   ├── static/
│   │   └── library/
│   │       └── style.css
│   ├── templates/
│   │   └── library/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── LibraryManagement/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── .gitignore
└── README.md
```

## Main Modules

### Books

The system stores:

* Book title
* Author
* ISBN
* Category
* Total copies
* Available copies
* Published year

### Students

Student records include:

* Name
* Email
* Phone number
* Department

### Book Transactions

The system tracks:

* Student
* Book
* Issue date
* Due date
* Return date
* Transaction status
* Fine amount

Books are issued for **14 days** by default. A fine is calculated automatically when a book is returned after the due date.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/LibraryManagement.git
cd LibraryManagement
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Django

```bash
pip install django
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### 5. Configure the database

This project is configured to use **MySQL**.

Create a MySQL database and update the database settings in:

```text
LibraryManagement/settings.py
```

Do not commit database passwords or secret keys to GitHub. Use environment variables for production.

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create an admin user

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 8. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser at:

```text
http://127.0.0.1:8000/
```

## Database Models

The application contains three main models:

* **Book**
* **Student**
* **IssueTransaction**

`IssueTransaction` connects students and books and keeps track of issue and return information.

## Fine Calculation

When a book is returned after its due date, the system calculates the fine based on the number of late days.

```text
Fine = Late Days × 10
```

## Future Improvements

* Book cover image uploads
* Advanced book search and filtering
* Email notifications for due dates
* Student profile pages
* Pagination
* Reports and analytics
* REST API
* Improved role-based permissions
* Deployment with production-ready configuration

## Author

Developed as a Django-based Library Management System project.

## License

This project is available for educational and personal use.
