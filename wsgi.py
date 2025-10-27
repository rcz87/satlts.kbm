"""
WSGI Entry Point untuk Production Server
Portal Satlantas Polres Kebumen

File ini adalah entry point untuk Gunicorn production server.
Gunakan file ini ketika deploy ke VPS dengan Gunicorn.

Cara menjalankan:
  gunicorn --bind 0.0.0.0:8000 wsgi:app
"""

from app import app

if __name__ == "__main__":
    app.run()
