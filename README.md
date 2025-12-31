# ScreenShot
<img width="839" height="378" alt="image" src="https://github.com/user-attachments/assets/4b95b4a2-15cd-403e-bd54-1dc360f93903" />


# URL Shortener (Flask)

A simple URL shortener built with Python and Flask.  
It takes a long URL, generates a short code, and redirects users back to the original link.

This project is intentionally minimal and focuses on core backend logic rather than extra features.

---

## Features
- Generate short URLs from long links
- Redirect short URLs using HTTP 302
- Basic input validation
- Clean and simple UI
- No external dependencies beyond Flask

---

## Tech Stack
- Python
- Flask
- HTML & CSS
- In-memory data storage

---

## How It Works
1. The user enters a long URL.
2. The app generates a random 6-character short code.
3. The short code is mapped to the original URL in memory.
4. Visiting the short URL redirects the user to the original link.

Note: Since storage is in-memory, all links reset when the server restarts.

---

## How to Run Locally(linux) never tied on windows sry

```bash
# create virtual environment
python3 -m venv venv # One-Time setup
source venv/bin/activate.fish
app.py
