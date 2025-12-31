# ScreenShot
<img width="952" height="1016" alt="image" src="https://github.com/user-attachments/assets/17ed0a02-e55e-4821-a0d0-03f69b7c5d07" />

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

## How to Run Locally

```bash
# create virtual environment
python3 -m venv venv
source venv/bin/activate.fish
app.py
