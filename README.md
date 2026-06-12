# A Clean, Minimalist Todo App

I built this lightweight task management web app using Python and Flask. Most todo tutorials you find online use overly flashy templates or massive JavaScript frameworks just to manage a simple list. I wanted to build something different: a clean, quiet, and highly functional workspace with a minimalist **Studio Grey & Matte Charcoal** look. 

It handles multiple task statuses, keeps data safe in a database, and completely avoids the generic "AI-generated SaaS" look by using a custom design built entirely from scratch.

---

##  The Tech Stack

* **Backend:** Flask (Python 3) using a clean application factory structure.
* **Blueprints:** Separated cleanly into `auth` (handling users) and `tasks` (handling the actual todo logic).
* **Database & ORM:** SQLite for simple data persistence, managed through Flask-SQLAlchemy.
* **Security:** Secure password hashing using `scrypt` via Werkzeug.
* **Frontend:** Server-rendered templates using Jinja2, styled with raw, custom CSS variables (no Tailwind, no Bootstrap).

---

##  Project Structure

Here is how the project files are organized:

```text
todo/
│
├── app/
│   ├── routes/
│   │   ├── __init__.py       # Sets up the blueprints
│   │   ├── auth.py           # Login, registration, and logout logic
│   │   └── tasks.py          # Creating, updating, and deleting tasks
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css     # Custom minimalist styling (zero blue tones)
│   │
│   ├── templates/
│   │   ├── base.html         # Main layout header, nav, and flash messages
│   │   ├── login.html        # Clean login screen
│   │   ├── register.html     # Signup screen
│   │   └── tasks.html        # The main dashboard workspace
│   │
│   ├── __init__.py           # Initializes the Flask app and database
│   └── models.py             # Database models for Users and Tasks
│
├── instance/
│   └── todo.db               # Your local SQLite database file
│
├── .gitignore                # Stops junk files from going to GitHub
└── run.py                    # The main entry point to start the app
