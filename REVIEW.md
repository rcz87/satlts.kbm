# Code Review: Portal Satlantas Polres Kebumen

**Tanggal Review:** 2026-02-15
**Reviewer:** Claude Code

---

## Ringkasan

Aplikasi web Flask untuk Portal Informasi Satlantas Polres Kebumen. Menyediakan informasi layanan SAMSAT, survei IKM (Indeks Kepuasan Masyarakat), feedback publik, dan panel admin.

## Temuan Kritis

### 1. XSS (Cross-Site Scripting) — `app_feedback.py:271-286`

Data user (`nama`, `email`, `pesan`) langsung diinterpolasi ke HTML tanpa escaping di route `/feedback/daftar`. Penyerang bisa menyuntikkan `<script>` melalui form feedback.

**Fix:** Gunakan `markupsafe.escape()` atau pindahkan ke Jinja2 template.

### 2. Mismatch Nama Tabel & Kolom — Admin vs IKM

- Admin dashboard (`app_admin.py:92`) query ke tabel `ikm_responses` dengan kolom `q1-q9`
- IKM submit (`app_ikm.py:69`) insert ke tabel `survei_ikm` dengan kolom `persyaratan, prosedur, ...`

Admin dashboard tidak akan menampilkan data IKM yang benar.

### 3. Mismatch Kolom Feedback — Admin vs Schema

- Admin (`app_admin.py:128`) query: `submitted_at, name, message`
- Tabel feedback (`app_feedback.py:60-68`): `created_at, nama, pesan`

Admin feedback view akan error karena kolom tidak ditemukan.

### 4. Hardcoded Fallback Secret Key — `app.py:14`

```python
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')
```

Jika env var tidak di-set, session cookies bisa di-forge.

### 5. Default Credentials Terlihat di Login Page

Template `admin/login.html` menampilkan default credentials (`admin / admin123`).

### 6. Information Leakage

Detail error/exception diekspos ke user di:
- `app.py:67`
- `app_admin.py:69`
- `app_ikm.py:206`
- `app_feedback.py:302`

## Temuan Medium

### 7. Tidak Ada File Size Limit pada Upload

Gallery dan document upload tidak membatasi ukuran file.

### 8. CREATE TABLE di Request Handler

`app_feedback.py:59-69` — schema creation di setiap request submit.

### 9. Duplikasi `get_db_connection()` di 4 File

Fungsi yang sama di-copy di `app.py`, `app_admin.py`, `app_feedback.py`, `app_ikm.py`.

### 10. Tidak Ada Connection Pooling

Setiap request membuka koneksi baru ke PostgreSQL.

### 11. Blueprint Limiter Tidak Berfungsi

`app_admin.py:13-16` — Limiter dibuat tanpa di-attach ke Flask app.

### 12. Inline HTML di Python

`app_feedback.py:136-296` dan `app_ikm.py:149-200` — ratusan baris HTML di f-string.

### 13. Route `/feedback/daftar` Tanpa Autentikasi

Menampilkan semua feedback termasuk nama dan email tanpa login.

## Temuan Minor

| # | Issue | Lokasi |
|---|---|---|
| 14 | `uv.lock` di-commit tapi juga di `.gitignore` | Root |
| 15 | Typo "galery" seharusnya "gallery" | Routes, folder, templates |
| 16 | Tidak ada database migration system | Keseluruhan |
| 17 | Tidak ada unit/integration test | Keseluruhan |
| 18 | Mixed Indonesian/English naming di schema | Database |
| 19 | `print()` dipakai untuk logging | `app_ikm.py:205` |
| 20 | Holiday list di `datetime.js` perlu update manual tiap tahun | `static/datetime.js` |

## Yang Sudah Baik

- CSRF protection aktif (Flask-WTF)
- Rate limiting pada submit routes
- Security headers lengkap (CSP, HSTS, X-Frame-Options)
- Parameterized SQL queries (mencegah SQL injection)
- `secure_filename()` untuk upload
- Secure session cookie configuration
- Logging dengan rotating file handler
- `.env` tidak di-commit

## Rekomendasi Prioritas

1. Fix XSS di `feedback_daftar_route`
2. Fix tabel/kolom mismatch antara admin dan IKM/feedback modules
3. Hapus default credentials dari login template
4. Tambah file size limit pada upload
5. Pindahkan inline HTML ke Jinja2 templates
6. Consolidate `get_db_connection()` ke satu module
7. Tambah autentikasi ke `/feedback/daftar` atau hapus route tersebut
