# SAMSAT SMART INFOBOARD - Kebumen Edition

## 📌 Overview
Aplikasi web interaktif berbasis Flask untuk menampilkan informasi publik SAMSAT Kebumen. Website membaca file Markdown (`samsat_infoboard.md`) dan menampilkannya dalam format HTML yang rapi dengan styling profesional.

**Tujuan Proyek:**
- Menyediakan informasi layanan STNK dan pajak kendaraan yang mudah diakses
- Menampilkan jam operasional, persyaratan dokumen, dan estimasi biaya
- Memudahkan masyarakat mendapatkan informasi melalui QR Code

## 🏢 Identitas Portal
- **Nama**: SAMSAT Kebumen
- **Alamat**: Jalan Tentara Pelajar No. 54, Kebumen
- **Mitra**: SATLANTAS POLRES KEBUMEN

## 🏗️ Project Architecture

### Struktur Folder
```
├── app.py                    # Flask application utama
├── samsat_infoboard.md       # Konten informasi dalam format Markdown
├── qr_generator.py           # Script generator QR Code
├── templates/
│   └── index.html           # Template HTML utama
├── static/
│   └── style.css            # Styling CSS profesional
├── .gitignore               # Git ignore file
└── replit.md                # Dokumentasi proyek
```

### Teknologi Stack
- **Backend**: Flask (Python 3.11)
- **Templating**: Jinja2
- **Markdown Parser**: python-markdown dengan extensions (tables, fenced_code, nl2br)
- **QR Code**: qrcode + Pillow
- **Styling**: Custom CSS dengan gradient dan responsive design

## 🎨 Fitur

### 1. Markdown to HTML Rendering
- Membaca `samsat_infoboard.md` dan mengkonversi ke HTML
- Support untuk tabel, heading, lists, dan formatting
- Error handling untuk file tidak ditemukan

### 2. Professional UI/UX
- Header dengan gradient biru (identitas Samsat)
- Tabel informasi yang rapi dan mudah dibaca
- Responsive design untuk mobile dan desktop
- Print-friendly styling

### 3. QR Code Generator
- Script terpisah untuk generate QR Code
- Otomatis detect URL dari Replit environment
- Option untuk custom URL
- High error correction level

## 📝 Recent Changes
- **18 Oktober 2025**: Inisialisasi proyek
  - Setup Flask application dengan Markdown rendering
  - Buat konten informasi SAMSAT Kebumen lengkap
  - Implementasi styling profesional dengan gradient
  - Tambahkan QR Code generator script

## 🚀 Cara Menjalankan

### Development
```bash
python app.py
```
Aplikasi akan berjalan di `http://0.0.0.0:5000`

### Generate QR Code
```bash
python qr_generator.py
```
Script akan menanyakan URL target dan nama file output.

## 📊 Konten Informasi

File `samsat_infoboard.md` berisi:
- Informasi umum dan kontak
- Jam operasional
- Daftar layanan (pendaftaran, perpanjangan, balik nama, mutasi)
- Metode pembayaran
- Persyaratan dokumen
- Estimasi biaya PKB
- Tips dan informasi penting
- Info denda keterlambatan
- Layanan digital

## 🎯 User Preferences
- Bahasa Indonesia untuk semua konten dan komentar
- Styling profesional untuk kantor pemerintahan
- Emoji untuk visual appeal
- Responsive dan mobile-friendly

## 🔧 Configuration
- Port: 5000 (sesuai standar Replit)
- Host: 0.0.0.0 (allow all hosts)
- Debug mode: Enabled untuk development
- Secret key: Menggunakan SESSION_SECRET dari environment

## 📱 Deployment Notes
- Aplikasi siap di-deploy via Replit Deployments
- QR Code dapat di-generate dengan URL production
- Print-friendly untuk buat poster/banner fisik

## 🔐 Environment Variables
- `SESSION_SECRET`: Secret key untuk Flask session (sudah tersedia)
- `REPL_SLUG`: Otomatis dari Replit (untuk QR code URL)
- `REPL_OWNER`: Otomatis dari Replit (untuk QR code URL)

---

*Dokumentasi ini akan di-update seiring perkembangan proyek*
