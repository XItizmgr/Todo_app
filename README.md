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
│   │   ├── __init__.py       
│   │   ├── auth.py           
│   │   └── tasks.py         
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css     
│   ├── templates/
│   │   ├── base.html        
│   │   ├── login.html        
│   │   ├── register.html    
│   │   └── tasks.html        
│   │
│   ├── __init__.py          
│   └── models.py           
│
├── instance/
│   └── todo.db              
│
├── .gitignore               
└── run.py                
