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

### **19 Oktober 2025 - Galeri Foto Lengkap & Footer Media Sosial Professional**
**Implementasi Galeri Foto Interaktif dengan 10 Foto Kegiatan**

#### Galeri Foto:
- ✅ 10 foto kegiatan SAMSAT Kebumen berhasil ditampilkan
- ✅ Grid layout responsive (3 kolom desktop, adaptive di mobile)
- ✅ Hover effects: foto zoom + caption muncul
- ✅ CSS styling profesional: rounded corners, shadows, smooth transitions
- ✅ Caption untuk setiap foto (pelayanan, sosialisasi, SAMKEL, dll)
- ✅ Gallery info box dengan daftar jenis kegiatan
- ✅ Mobile-friendly: caption visible permanen di mobile

#### Footer Media Sosial:
- ✅ Social media icons dengan **warna brand permanen** (bukan hanya hover)
- ✅ Instagram: Pink gradient + border orange
- ✅ Facebook: Blue background #1877f2 + border biru
- ✅ X (Twitter): Black background + white border
- ✅ TikTok: Black background + red-pink border
- ✅ Hover effects: translateY, scale, colored shadows
- ✅ SVG icons profesional (bukan emoji)

### **18 Oktober 2025 - Tambah Menu Galery**
- ✅ Menu "📸 Galery" untuk dokumentasi foto kegiatan SAMSAT
- ✅ Folder static/images/galery/ untuk foto-foto kegiatan

---

## 🚀 Rencana Pengembangan Kedepan

### Visi Project
Website SAMSAT SMART INFOBOARD ini adalah **menu kecil** dari rencana besar untuk membangun **Website Resmi Satlantas Polres Kebumen** yang lebih lengkap dan interaktif.

### Konsep Website Besar Satlantas Polres Kebumen

#### 🏢 Tampilan & Fitur Utama:
- **Hero Section Interaktif**: 
  - Gambar gedung Satlantas Polres Kebumen
  - Slideshow foto kegiatan dan pelayanan
  - Banner informasi penting dan pengumuman
  
- **Profil Satlantas**:
  - Visi dan Misi Satlantas Polres Kebumen
  - Struktur Organisasi
  - Sejarah dan pencapaian
  - Galeri foto gedung dan fasilitas

- **Informasi Pelayanan Interaktif**:
  - Jam pelayanan masing-masing unit
  - Peta lokasi dan denah gedung
  - Nomor kontak langsung setiap unit
  - Live chat customer service

#### 📋 Menu-Menu Pelayanan Utama:

1. **Unit Regident (Registrasi dan Identifikasi)**
   - Pelayanan SIM (Surat Izin Mengemudi)
     - SIM A, B1, B2, C, D
     - Perpanjangan SIM
     - SIM Hilang/Rusak
     - Jadwal ujian SIM
     - Booking online ujian SIM
   - Pelayanan BPKB (Buku Pemilik Kendaraan Bermotor)
   - Pelayanan STNK (Surat Tanda Nomor Kendaraan)
     - SAMSAT SMART INFOBOARD (website saat ini akan menjadi sub-menu)
     - Pembayaran pajak tahunan
     - Pembayaran pajak 5 tahunan
     - BBN 1 dan BBN 2
     - Mutasi kendaraan
   - Cek status pelayanan online

2. **Unit Gakum (Penegakan Hukum)**
   - Sub-Unit Laka Lantas (Kecelakaan Lalu Lintas)
     - Prosedur lapor kecelakaan
     - Investigasi kecelakaan
     - Statistik kecelakaan di Kebumen
     - Tips pencegahan kecelakaan
   - Sub-Unit Tilang (Pelanggaran Lalu Lintas)
     - Jenis-jenis pelanggaran
     - Cara bayar tilang online
     - Cek tilang belum dibayar
     - Jadwal sidang tilang
     - Edukasi aturan lalu lintas

3. **Unit Patwal (Patroli Jalan Raya)**
   - Jadwal patroli harian
   - Titik-titik rawan kecelakaan
   - Info kemacetan real-time (integrasi TMC)
   - Himbauan keselamatan berkendara
   - Kontak darurat Patwal

4. **Unit Kamsel (Keamanan dan Keselamatan)**
   - Program keselamatan berkendara
   - Safety riding campaign
   - Edukasi keselamatan untuk pelajar
   - Partnership dengan sekolah dan komunitas
   - Jadwal sosialisasi keselamatan

5. **Unit Urmin (Urusan Umum)**
   - Pengaduan masyarakat
   - Saran dan kritik
   - Transparansi anggaran
   - Pengumuman lelang/tender
   - Informasi kepegawaian

6. **Unit TMC (Traffic Management Center)**
   - Live CCTV lalu lintas (jika tersedia)
   - Info kemacetan real-time
   - Info cuaca dan kondisi jalan
   - Peta interaktif Kebumen
   - Rute alternatif

#### 🎯 Fitur Interaktif Tambahan:

- **Dashboard Publik**:
  - Statistik pelayanan real-time
  - Grafik jumlah SIM yang diterbitkan
  - Data kecelakaan per bulan
  - Tingkat kepuasan masyarakat (IKM)
  
- **Portal Masyarakat**:
  - Registrasi akun warga
  - Tracking status permohonan
  - Riwayat transaksi pelayanan
  - Download dokumen pelayanan
  
- **Sistem Antrian Online**:
  - Booking antrian pelayanan
  - Estimasi waktu tunggu
  - Notifikasi SMS/WhatsApp
  
- **Media Center**:
  - Berita dan kegiatan Satlantas
  - Siaran pers
  - Video edukasi lalu lintas
  - Podcast keselamatan berkendara
  - Galeri foto dan video kegiatan
  
- **Integrasi Media Sosial**:
  - Instagram feed live
  - Twitter/X timeline
  - Facebook updates
  - TikTok videos embed
  - YouTube channel embed

#### 💡 Teknologi yang Direncanakan:

- **Backend**: Flask/Python atau Django (untuk sistem yang lebih besar)
- **Frontend**: React.js atau Vue.js (untuk interaktivitas tinggi)
- **Database**: PostgreSQL (untuk data besar dan relasi kompleks)
- **Real-time**: WebSocket untuk update live (antrian, CCTV, info lalu lintas)
- **Maps**: Google Maps API atau OpenStreetMap
- **Notification**: SMS Gateway, WhatsApp Business API
- **Security**: Tetap mengikuti OWASP Top 10 dan BSSN standards
- **Hosting**: Cloud hosting dengan auto-scaling untuk traffic tinggi

#### 📱 Mobile Responsive:

- Progressive Web App (PWA)
- Optimized untuk smartphone
- Offline mode untuk informasi penting
- Push notification untuk pengumuman

### Tahapan Pengembangan:

**Phase 1 (SELESAI)**: 
✅ SAMSAT SMART INFOBOARD - Kebumen Edition (Website saat ini)

**Phase 2 (NEXT)**: 
- Landing page Satlantas Polres Kebumen
- Profil dan struktur organisasi
- Menu navigasi ke semua unit

**Phase 3**: 
- Pengembangan portal Unit Regident lengkap
- Sistem booking online SIM
- Integrasi pembayaran online

**Phase 4**: 
- Portal Unit Gakum (Laka Lantas & Tilang)
- Sistem tracking laporan kecelakaan
- Payment gateway untuk tilang online

**Phase 5**: 
- Portal Unit Patwal dan Kamsel
- Live tracking patroli (jika memungkinkan)
- Dashboard TMC dengan info real-time

**Phase 6**: 
- Integrasi semua unit
- Mobile app development
- Advanced analytics dan reporting

### Catatan Penting:
Website SAMSAT SMART INFOBOARD saat ini akan tetap berfungsi sebagai **standalone application** dan juga akan menjadi **sub-menu di bawah Unit Regident** pada website besar nantinya. Semua data dan fitur akan diintegrasikan ke sistem yang lebih besar.
