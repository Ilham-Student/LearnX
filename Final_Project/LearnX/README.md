# LearnX (Django) — YouTube‑powered course platform

This is a complete Django project scaffold for **LearnX**, built to your spec:
- Modular apps: `accounts`, `courses`, `quizzes`, `progress_app`, `certificates`, `core`, `admin_tools`
- **Common templates** folder (`templates/`) used by all apps
- **Static** folder with CSS & JS; your CSS is referenced globally from `static/css/style.css`
- Contact form with **JS validation** and email sending to admin
- Import **YouTube videos via API** (duration included) with management command
- **Auto‑generate quizzes** from YouTube video transcripts
- Track **progress** and generate **PDF certificates** (with serial and QR)
- Compatible with **Python 3.13** and **Django 5.1+**

> ⚠️ If you already have a `requirements.txt` in your repo with strict pins, keep it. Append the **new libraries** from this project's `requirements.txt` to yours. The versions chosen here work with Python 3.13.

## Quick start

```bash
# 1) Create & activate a virtualenv (Python 3.13)
python3.13 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3) Add environment variables
cp .env.example .env
# Edit .env with your keys & email settings

# 4) DB setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 5) Collect static (optional for prod)
python manage.py collectstatic

# 6) Run
python manage.py runserver
```

## Environment variables (`.env`)

```
DEBUG=True
SECRET_KEY=dev-secret-change-me

# Allowed hosts (comma-separated) e.g. 127.0.0.1,localhost
ALLOWED_HOSTS=localhost,127.0.0.1

# YouTube
YOUTUBE_API_KEY=YOUR_YOUTUBE_DATA_API_V3_KEY

# Email (choose one backend)
# For development, console backend (prints emails to terminal)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# For Gmail SMTP (requires App Password, not your login)
# EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=yourgmail@gmail.com
# EMAIL_HOST_PASSWORD=your_app_password  # 16-char app password from Google
DEFAULT_FROM_EMAIL=LearnX <no-reply@learnx.local>
CONTACT_EMAIL=admin@example.com
```

### Gmail SMTP tip
Use a **Google App Password** with 2FA enabled; put that in `EMAIL_HOST_PASSWORD`. Do **not** use your normal password. See notes in docs and community threads about Gmail SMTP + Django. 

### Importing YouTube videos
- Create a Course in Django admin first.
- Get a YouTube **Playlist ID** (or individual video IDs).  
- Run:

```bash
python manage.py import_youtube --course <COURSE_ID> --playlist <PLAYLIST_ID>
# or single video
python manage.py import_youtube --course <COURSE_ID> --video <VIDEO_ID>
```

This fetches title/description and **duration** and stores `Video` objects.

### Auto‑generated quizzes from transcripts
When a `Video` is saved, we try to fetch its transcript using `youtube-transcript-api`.  
If available, we generate a small MCQ quiz (NER/keyword based heuristics using NLTK).  
You can also (re)generate via admin action or directly from the Video detail page button we added.

> Note: Transcripts aren’t available for all videos; private/disabled/copyrighted transcripts will be skipped gracefully.

### Certificates
When a user completes all course videos and has attempted any quizzes attached to those videos, a PDF certificate can be generated and downloaded. The certificate includes a **serial** and **QR** code that points to a verify endpoint.

### Common templates & your CSS
- All templates live in `/templates`. The **base layout** is `templates/base.html` and includes your stylesheet: `static/css/style.css`. Replace that file with your own CSS to carry your design globally.

## Apps Overview

- `accounts`: custom user (role: `learner`/`admin`), auth & dashboard
- `courses`: Course/Video models, YouTube import command
- `quizzes`: Quiz/Question/Choice/Submission, transcript → MCQs
- `progress_app`: watched/complete tracking
- `certificates`: PDF generator with ReportLab + QR
- `core`: home, contact form (+JS validation)
- `admin_tools`: simple stats (extend as needed)

## Known limits & notes
- We prefer **ReportLab** for certificates to avoid system deps needed by WeasyPrint.
- NLTK downloads small models at runtime if missing on first quiz generation.
- If you keep your original `requirements.txt`, ensure **Django 5.1+** for Python 3.13 compatibility.

## License
Use and modify freely for your course project.
