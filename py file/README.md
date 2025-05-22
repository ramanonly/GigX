#  GigX Platform - Final submission of internship
A full-stack Django application for managing gig listings—allowing providers to post gigs, seekers to browse and favorite gigs, and both to have personalized dashboards.

## Features
- Provider Dashboard to view their gigs
- Seeker Dashboard with favorites
- Favorite/unfavorite gigs
- Authentication (register/login/logout)
*Environment Configuration
  - Sensitive settings (e.g. `SECRET_KEY`) stored in `.env` and loaded via `python-decouple`. 
*Static & Templates 
  - Responsive HTML templates using Django Template Language (DTL).  
  - External CSS in `static/users/styles.css`.

## ⚙ Technologies
Backend: Django 5.x, Django REST Framework
Database: SQLite
Auth & Env: python-decouple for .env
Frontend: Django templates (DTL), HTML, CSS
Testing: Postman (for API endpoints)

## 🧪 Setup Instructions
git clone <your-repo>
cd gigx-platform
python -m venv .venv
.venv\Scripts\activate 
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
