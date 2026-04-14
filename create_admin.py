#!/usr/bin/env python3
"""
Bootstrap admin user untuk Portal Satlantas.

Usage:
    python create_admin.py                    # interaktif
    python create_admin.py <username> <full_name>   # password via env ADMIN_PASSWORD atau prompt

Contoh:
    python create_admin.py admin "Admin Satlantas"
"""
import os
import sys
import getpass

from werkzeug.security import generate_password_hash
from db import get_db_connection, init_tables


def create_admin(username: str, full_name: str, password: str) -> None:
    init_tables()
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id FROM admin_users WHERE username = %s", (username,))
        existing = cur.fetchone()
        pw_hash = generate_password_hash(password)
        if existing:
            cur.execute(
                "UPDATE admin_users SET password_hash = %s, full_name = %s, is_active = TRUE WHERE username = %s",
                (pw_hash, full_name, username),
            )
            print(f"[OK] Password & data admin '{username}' di-update.")
        else:
            cur.execute(
                "INSERT INTO admin_users (username, password_hash, full_name, is_active) VALUES (%s, %s, %s, TRUE)",
                (username, pw_hash, full_name),
            )
            print(f"[OK] Admin '{username}' berhasil dibuat.")
        conn.commit()
    finally:
        cur.close()
        conn.close()


def main() -> int:
    if len(sys.argv) >= 3:
        username = sys.argv[1]
        full_name = sys.argv[2]
    else:
        username = input("Username: ").strip()
        full_name = input("Nama lengkap: ").strip()

    if not username or not full_name:
        print("Username dan nama lengkap wajib diisi.", file=sys.stderr)
        return 1

    password = os.environ.get("ADMIN_PASSWORD") or getpass.getpass("Password: ")
    if not password or len(password) < 8:
        print("Password minimal 8 karakter.", file=sys.stderr)
        return 1

    if not os.environ.get("ADMIN_PASSWORD"):
        confirm = getpass.getpass("Ulangi password: ")
        if password != confirm:
            print("Password tidak cocok.", file=sys.stderr)
            return 1

    try:
        create_admin(username, full_name, password)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
