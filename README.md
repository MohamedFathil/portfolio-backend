# 🚀 Mohamed Fathil — Portfolio

A professional full-stack portfolio with a **React** (Vite) frontend and a **Django REST Framework** backend.

---

## 📁 Project Structure

```
portfolio/
├── portfolio-frontend/        # React + Vite
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── About.jsx
│   │   │   ├── Skills.jsx
│   │   │   ├── Experience.jsx
│   │   │   ├── Projects.jsx
│   │   │   ├── Certifications.jsx
│   │   │   └── Contact.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
│
└── portfolio-backend/         # Django REST API
    ├── api/
    │   ├── models.py          # ContactMessage, Project, Skill, Certification
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   └── management/
    │       └── commands/
    │           └── seed_data.py
    ├── portfolio_backend/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── requirements.txt
```

---

## ⚡ Quick Start

### 1 — Backend (Django)

```bash
cd portfolio-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies (SQLite version — no MySQL needed for dev)
pip install django djangorestframework django-cors-headers gunicorn

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Seed portfolio data (projects, skills, certs)
python manage.py seed_data

# Create admin superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
# API is live at http://localhost:8000
```

### 2 — Frontend (React + Vite)

```bash
cd portfolio-frontend

npm install
npm run dev
# App is live at http://localhost:5173
```

---

## 🔗 API Endpoints

| Method | Endpoint              | Description                    |
|--------|-----------------------|--------------------------------|
| GET    | /api/summary/         | Portfolio stats & info         |
| GET    | /api/projects/        | All featured projects          |
| GET    | /api/skills/          | Skills grouped by category     |
| GET    | /api/certifications/  | All certifications             |
| POST   | /api/contact/         | Submit a contact message       |

### POST /api/contact/ — Body
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Job Opportunity",
  "message": "Hi Mohamed, I'd like to discuss..."
}
```

---

## 🛠 Admin Panel

Visit `http://localhost:8000/admin/` after creating a superuser to:
- View & manage contact messages (mark as read)
- Add/edit projects, skills, certifications

---

## 🌐 Production Deployment

### Backend
1. Set `DEBUG = False` in `settings.py`
2. Set a strong `SECRET_KEY` via environment variable
3. Switch to MySQL in `DATABASES` settings
4. Run `python manage.py collectstatic`
5. Serve with `gunicorn portfolio_backend.wsgi:application`
6. Use Nginx as a reverse proxy

### Frontend
```bash
npm run build
# Deploy the /dist folder to Nginx, Vercel, or Netlify
```

### Environment Variables (production)
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DB_NAME=portfolio_db
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=localhost
EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

---

## ✨ Features

- 🌑 Dark theme with cyan/violet gradient accents
- 🎨 3D floating hero card with CSS animation
- ✨ Hover effects on all cards (lift + glow)
- 📱 Fully responsive (mobile, tablet, desktop)
- 🔄 Slide-in / fade-up entrance animations
- 📬 Working contact form → saves to DB + sends email
- 🔧 Django Admin dashboard to manage all content
- 🌐 REST API — frontend can be swapped or extended

---

Built with ❤️ by **Mohamed Fathil** · Abu Dhabi, UAE
