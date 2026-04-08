# BookSocialMedia

A social media aimed at publishing quotes and ideas about books, we can create posts, add books (which will first be validated by admin), create book clubs and comment posts.

---

## Features

- Post your quotes and reflections about specific books
- Brows post by genre and books
- Create, Join and Leave😒 book clubs(for now book club is not very interactive)
- Comment on posts🤩
- Activity feed showing recent comments
- login, register and logout

---

## Tech Stack

- **Backend:** Python, Django 
- **Frontend:** HTML, CSS, Bootstrap 5
- **Forms** django_crispy_forms with crispy-bootstrap5
- **Database** SQLite

---

## Prerequisites

- Python 3.11+
- Django 6

---

## Installation

### 1. Clone repo

```bash
git clone https://github.com/KGeox/BookSocialMedia.git
cd BookSocial Media
```
I uploaded with my venv so you can just delete it and make your own or continue with mine

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/linux:
source venv/bin/activate
```
### 3. Install dependencies

```bash
pip install django crispy-forms crispy-bootstrap5 pillow
```

> 'pillow' is required for image fields (profil pictures and all images in general)

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (admin account)

``` bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

It will be available at `http://127.0.0.1:8000/`

---

## Usage

### As a regular user

1. Go to '/register' and create an account
2. Add a book at 'create-book' - ( You must go on admin page to validate it if not it will not appear)
3. Create a post at '/create-post/' - link it to a book and say what you wan't to say
4. Create and visit clubs
5. Edit your profile
6. Read the post

### As an admin

1. Go to '/admin' and log in with your superuser
2. From the admin dashboard you can manage the Books, posts, users and clubs

---

## Project Structure

```
BookSocialMedia/
│
├── BookSocialMedia/        # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── main/                   # Main app
│   ├── models.py           # Profile, Book, Post, Comment, BookClub
│   ├── views.py            # All view logic
│   ├── forms.py            # ModelForms for Post, Book, Profile, BookClub
│   ├── urls.py             # App URL routes
│   └── apps.py
│
├── templates/
│   └── main/               # All HTML templates
│       ├── base.html
│       ├── home.html
│       ├── post.html
│       ├── book.html
│       ├── profile.html
│       ├── edit_profile.html
│       ├── post_form.html
│       ├── bookclub_list.html
│       ├── bookclub_detail.html
│       ├── login_register.html
│       ├── delete.html
│       ├── navbar.html
│       ├── feed_component.html
│       ├── topics_component.html
│       └── activity_component.html
│
├── static/
│   └── styles/
│       └── main.css
│
├── media/                  # Uploaded images (auto-created)
├── db.sqlite3              # Database (auto-created)
└── README.md
```

---

## License

This Project is for personal or educational use.

