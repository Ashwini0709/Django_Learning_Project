# SmartNotes

SmartNotes is a Django-based web application that allows users to create, manage, and organize personal notes securely. It supports user authentication and provides the ability to make notes either **public** or **private**.

## Features

- ✍️ Create notes with a **title** and **text content**
- 🔐 **User authentication** (login, logout, registration)
- 🔒 **Private notes**: visible and editable only by the note's owner after login
- 🌍 **Public notes**: visible to all users, even without authentication
- 🧾 Clean, simple, and intuitive user interface

## Usage

1. Register or log in to your account
2. Create notes and choose whether they are public or private
3. View public notes without logging in
4. Edit or delete your notes after logging in

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates, HTML, Bootstrap
- **Database:** SQLite (default for development)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smartnotes.git
   cd smartnotes

2. Create and activate a virtual environment:
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install dependencies:
    pip install django

4. Apply migrations:
    python manage.py migrate
   
5. Run the development server:
    python manage.py runserver

6. Visit http://127.0.0.1:8000/ in your browser to start using SmartNotes.


