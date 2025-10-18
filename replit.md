# SAMSAT SMART INFOBOARD - Kebumen Edition

## Overview
This Flask-based web application, SAMSAT SMART INFOBOARD - Kebumen Edition, provides an interactive platform for the public to access essential information regarding SAMSAT Kebumen services. Its primary purpose is to offer easily accessible information on vehicle registration (STNK) and tax, operating hours, required documents, and estimated costs. The project aims to streamline information dissemination through a professional, user-friendly interface, enhancing public access via QR code integration.

## User Preferences
- Bahasa Indonesia untuk semua konten dan komentar
- Styling profesional untuk kantor pemerintahan
- Emoji untuk visual appeal
- Responsive dan mobile-friendly

## System Architecture
The application is built using Flask, serving content dynamically rendered from Markdown files for each service category. It features a multi-page architecture with 8 main menus: Home, 5-Year Tax, Duplicate STNK, Inter-regional Transfer, BBN 1 & 2, Legal Basis, Gallery, and IKM (Community Satisfaction Index). The UI/UX emphasizes a professional design with a blue gradient header, responsive navigation, and print-friendly styling. Legal documents are presented with embedded PDF viewers, and a dedicated gallery showcases SAMSAT activities. A fully functional IKM survey system is integrated, allowing users to rate service aspects via a star rating system and submit comments, with results displayed on a real-time dashboard. The IKM system calculates a satisfaction score based on 9 criteria, categorized from "Sangat Baik" to "Tidak Baik" according to Permenpan RB No. 14/2017.

### Folder Structure
```
├── app.py                    # Main Flask application with multi-page routes
├── app_ikm.py                # Module for IKM routes (submit & results)
├── content_home.md           # Homepage content
├── content_5tahunan.md       # 5-yearly tax requirements content
├── content_duplikat.md       # Duplicate STNK content
├── content_mutasi.md         # Inter-regional transfer content
├── content_bbn.md            # BBN 1 and BBN 2 content
├── content_dasarhukum.md     # Legal basis and regulations content
├── content_galery.md         # SAMSAT activity gallery content
├── content_ikm.md            # IKM survey content + interactive form
├── qr_generator.py           # QR Code generator script
├── templates/
│   └── index.html           # HTML template with navigation menu + ikm.js
├── static/
│   ├── style.css            # Professional CSS styling with IKM styles
│   ├── ikm.js               # JavaScript for star rating & AJAX submit
│   ├── images/
│   │   ├── logo-samsat.png  # Official SAMSAT logo
│   │   └── galery/          # Folder for activity photos
│   └── documents/
│       ├── perpol-7-2021-regident.pdf  # Police Regulation No. 7/2021
│       └── uu-22-2009-lalulintas.pdf   # Law No. 22/2009 Traffic
├── .gitignore               # Git ignore file
└── replit.md                # Project documentation
```

## External Dependencies
- **Backend Framework**: Flask (Python 3.11)
- **Database**: PostgreSQL (Neon) for IKM survey data
- **Templating Engine**: Jinja2
- **Markdown Parser**: python-markdown with extensions (tables, fenced_code, nl2br)
- **QR Code Generation**: qrcode + Pillow
- **Frontend Interactivity**: Vanilla JavaScript (for star rating, AJAX)
- **Security**: Flask-WTF (CSRF protection), Flask-Limiter (rate limiting)

## 🔒 Security Features
Website ini mengikuti standar keamanan OWASP Top 10 2021 dan persyaratan keamanan pemerintah Indonesia (BSSN):

### Protection Mechanisms:
- **CSRF Protection**: Flask-WTF dengan token validation di semua form submissions
- **SQL Injection Prevention**: Parameterized queries dengan psycopg2
- **XSS Prevention**: Jinja2 auto-escaping + CSP headers
- **Rate Limiting**: 200 requests/day umum, 10 requests/hour untuk IKM submit
- **Input Validation**: Whitelist validation untuk jenis layanan (8 tipe yang diizinkan)
- **Security Headers**:
  - X-Frame-Options: SAMEORIGIN (anti-clickjacking)
  - X-Content-Type-Options: nosniff (anti-MIME sniffing)
  - X-XSS-Protection: 1; mode=block
  - Content-Security-Policy: Strict CSP rules
  - Referrer-Policy: strict-origin-when-cross-origin
  - Strict-Transport-Security (HSTS) untuk production
- **Secure Session**: HttpOnly, Secure, SameSite cookies
- **HTTPS Enforcement**: HSTS headers di production mode

## 📝 Recent Changes

### **18 Oktober 2025 - Implementasi Keamanan Komprehensif**
**Perlindungan Maksimal dari Serangan Hacker sesuai OWASP Top 10 & BSSN Standards**

#### Security Enhancements:
- ✅ CSRF Protection menggunakan Flask-WTF dengan token validation
- ✅ Rate Limiting untuk mencegah DDoS dan spam (Flask-Limiter)
- ✅ Security Headers lengkap (X-Frame-Options, CSP, HSTS, X-Content-Type, Referrer-Policy)
- ✅ Input validation whitelist untuk dropdown jenis_layanan
- ✅ CSRF token integration di templates dan JavaScript AJAX
- ✅ Secure session configuration (HttpOnly, Secure, SameSite flags)
- ✅ HTTPS enforcement configuration untuk deployment
- ✅ Tested dan verified semua security features aktif

### **18 Oktober 2025 - Implementasi Lengkap Sistem IKM**
**Sistem Survei Kepuasan Masyarakat Fully Functional dengan Database PostgreSQL**

#### Database & Backend:
- ✅ Tabel `survei_ikm` di PostgreSQL dengan 14 kolom (id, created_at, 9 aspek rating, komentar, jenis_layanan, rata_rata)
- ✅ Module `app_ikm.py` terpisah untuk routes IKM (maintainability & separation of concerns)
- ✅ Route `/ikm` - menampilkan form survei interaktif
- ✅ Route `/ikm/submit` - API endpoint (POST, JSON) untuk menerima data survei dengan validasi lengkap
- ✅ Route `/ikm/hasil` - dashboard hasil publik real-time dengan statistik dan visualisasi
- ✅ Server-side validation untuk jenis_layanan (required) dan rating values (1-4)
- ✅ Structured logging dengan level appropriate (info, warning, error)
- ✅ Error handling dengan specific exception types (ValueError, psycopg2.Error, Exception)
- ✅ Database indexes untuk performance: `idx_survei_ikm_jenis_layanan`, `idx_survei_ikm_created_at`

#### Frontend & Interactivity:
- ✅ Form HTML interaktif dengan 9 rating items + dropdown + textarea
- ✅ JavaScript `static/ikm.js` untuk star rating, form validation, AJAX submission
- ✅ CSS styling lengkap: star rating system, progress bars, responsive cards, color-coded categories

#### Features:
- ✅ 9 aspek penilaian sesuai Permenpan RB No. 14/2017
- ✅ Star rating system (1-4 bintang) dengan visual feedback
- ✅ Perhitungan IKM otomatis: AVG(rata_rata) × 25
- ✅ Kategorisasi hasil: A (88.31-100), B (76.61-88.30), C (65.00-76.60), D (25.00-64.99)
- ✅ Dashboard hasil dengan nilai IKM, total responden, breakdown per aspek dengan progress bars
- ✅ Code reviewed by architect - no security issues, following best practices

### **18 Oktober 2025 - Tambah Menu Galery**
- ✅ Menu "📸 Galery" untuk dokumentasi foto kegiatan SAMSAT
- ✅ Folder static/images/galery/ untuk foto-foto kegiatan
