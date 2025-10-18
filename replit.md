# SAMSAT SMART INFOBOARD - Kebumen Edition

## 📌 Overview
Aplikasi web interaktif berbasis Flask untuk menampilkan informasi publik SAMSAT Kebumen. Website membaca file Markdown terpisah untuk setiap kategori layanan dan menampilkannya dalam format HTML yang rapi dengan styling profesional.

**Tujuan Proyek:**
- Menyediakan informasi layanan STNK dan pajak kendaraan yang mudah diakses
- Menampilkan jam operasional, persyaratan dokumen, dan estimasi biaya
- Memudahkan masyarakat mendapatkan informasi melalui QR Code

## 🏢 Identitas Portal
- **Nama**: SAMSAT Kebumen
- **Alamat**: Jalan Tentara Pelajar No. 54, Kebumen
- **Petugas Pelayanan**: SATLANTAS POLRES KEBUMEN

## 🏗️ Project Architecture

### Struktur Folder
```
├── app.py                    # Flask application utama dengan multi-page routes
├── content_home.md           # Konten halaman beranda
├── content_5tahunan.md       # Konten syarat pembayaran 5 tahunan
├── content_duplikat.md       # Konten duplikat STNK
├── content_mutasi.md         # Konten mutasi antar daerah
├── content_bbn.md            # Konten BBN 1 dan BBN 2
├── qr_generator.py           # Script generator QR Code
├── templates/
│   └── index.html           # Template HTML dengan navigasi menu
├── static/
│   ├── style.css            # Styling CSS profesional dengan active state
│   └── documents/
│       └── perpol-7-2021-regident.pdf  # Peraturan Kepolisian No. 7/2021
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

### 1. Multi-Page Architecture
- Halaman terpisah untuk setiap kategori layanan
- 6 menu utama: Beranda, Syarat 5 Tahunan, Duplikat STNK, Mutasi Antar Daerah, BBN 1 & 2, Perpol 7/2021
- Navigasi menu sticky dengan active state highlighting (golden border)
- Setiap halaman memuat konten Markdown yang spesifik
- Menu Perpol 7/2021 menampilkan PDF embedded viewer untuk peraturan resmi

### 2. Markdown to HTML Rendering
- Membaca file Markdown terpisah untuk setiap halaman
- Support untuk tabel, heading, lists, dan formatting
- Error handling untuk file tidak ditemukan
- Helper function untuk load dan render Markdown

### 3. Professional UI/UX
- Header dengan gradient biru (identitas Samsat)
- Navigasi menu responsif dengan hover dan active state
- Tabel informasi yang rapi dan mudah dibaca
- Responsive design untuk mobile dan desktop
- Print-friendly styling
- Footer dengan informasi kontak dan link media sosial (Instagram, Facebook, X/Twitter, TikTok)

### 4. QR Code Generator
- Script terpisah untuk generate QR Code
- Otomatis detect URL dari Replit environment
- Option untuk custom URL
- High error correction level

### 5. PDF Viewer untuk Perpol 7/2021
- Embedded PDF viewer menggunakan iframe
- Menampilkan Peraturan Kepolisian No. 7/2021 tentang Regident Ranmor
- Opsi download PDF untuk akses offline
- File PDF disimpan di static/documents/

## 📝 Recent Changes
- **18 Oktober 2025**: Tambah Logo SAMSAT Resmi di Header
  - ✅ Logo resmi SAMSAT dengan lambang Garuda Pancasila dan sayap emas
  - ✅ Posisi di header sebelah kiri sebelum judul
  - ✅ Ukuran 140px (desktop) dan 110px (mobile) dengan responsive design
  - ✅ Efek hover dengan zoom scale 1.05
  - ✅ Shadow effect untuk depth visual
  - ✅ Logo tampil di semua halaman website
  - ✅ File tersimpan di static/images/logo-samsat.png
- **18 Oktober 2025**: Update Tombol WhatsApp di Footer
  - ✅ Tambahkan tombol WhatsApp hijau dengan logo 💬
  - ✅ Tombol bisa diklik langsung menuju chat WhatsApp
  - ✅ Styling dengan warna hijau khas WhatsApp (#25D366)
  - ✅ Efek hover dengan animasi (warna berubah dan naik sedikit)
  - ✅ Link aman dengan target="_blank" dan rel="noopener noreferrer"
- **18 Oktober 2025**: Tambah Informasi OPSEN Pajak 2025
  - ✅ Tambahkan penjelasan OPSEN di halaman Beranda (info umum tentang OPSEN)
  - ✅ Tambahkan section OPSEN lengkap di halaman 5 Tahunan (cara hitung, contoh)
  - ✅ Update semua contoh perhitungan biaya termasuk OPSEN (66% dari PKB)
  - ✅ Tambahkan OPSEN di halaman Mutasi (contoh perhitungan mutasi masuk)
  - ✅ Tambahkan OPSEN di halaman BBN 1 & BBN 2 (semua contoh perhitungan)
  - ✅ Jelaskan kenapa nominal OPSEN berbeda-beda (domisili & tarif provinsi)
- **18 Oktober 2025**: Hapus Biaya Cek Fisik
  - ✅ Hapus biaya Cek Fisik Rp 50.000 dari halaman Duplikat STNK (tidak ada biaya tersebut)
  - ✅ Update total biaya duplikat: Motor Rp 100.000, Mobil Rp 200.000
  - ✅ Biaya yang berlaku hanya Penerbitan STNK sesuai PNBP resmi
- **18 Oktober 2025**: Tambah Footer Kontak & Media Sosial
  - ✅ Tambahkan section kontak dengan WhatsApp (+62 877-2555-8787) dan alamat kantor
  - ✅ WhatsApp link langsung buka chat di wa.me
  - ✅ Tambahkan link media sosial: Instagram, Facebook, X (Twitter), TikTok
  - ✅ Styling interaktif dengan hover effects untuk setiap platform
  - ✅ Responsive design untuk mobile dan desktop
  - ✅ Footer muncul di semua halaman website
- **18 Oktober 2025**: Tambah Menu Perpol 7/2021
  - ✅ Tambahkan menu baru "Perpol 7/2021" dengan embedded PDF viewer
  - ✅ Upload dan integrasikan Peraturan Kepolisian No. 7/2021 tentang Regident Ranmor
  - ✅ Buat route /perpol dengan tampilan PDF viewer dan tombol download
  - ✅ File PDF tersimpan di static/documents/ untuk akses publik
- **18 Oktober 2025**: Update Tarif PNBP sesuai PP 76/2020 (Final)
  - ✅ Update tarif Mutasi Keluar: Motor Rp 150.000, Mobil Rp 250.000
  - ✅ Tambah informasi Pengesahan STNK Tahunan di halaman 5 Tahunan: Motor Rp 25.000/tahun, Mobil Rp 50.000/tahun
  - ✅ Semua tarif sudah terverifikasi sesuai PP 76/2020 oleh architect
  - ✅ Hapus semua biaya administrasi dari semua halaman
  - ✅ Update jam operasional Sabtu menjadi 08:00-12:00 WIB
- **18 Oktober 2025**: Implementasi multi-page architecture
  - Pisahkan konten ke 5 file Markdown terpisah (home, 5tahunan, duplikat, mutasi, BBN)
  - Buat routes Flask terpisah untuk setiap halaman (/,  /5tahunan, /duplikat, /mutasi, /bbn)
  - Implementasi navigasi menu dengan active state highlighting
  - Update branding dari "CV Cakra Pamungkas Mandiri" ke "SATLANTAS POLRES KEBUMEN"
  - Tambahkan helper function load_markdown untuk DRY code
  - Setup styling CSS untuk active menu dengan golden border
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

Konten dibagi ke dalam 5 file Markdown terpisah:

### content_home.md (Beranda)
- Sambutan singkat dan welcome message
- Lokasi dan kontak SAMSAT Kebumen
- Jam operasional
- Petunjuk untuk memilih menu sesuai kebutuhan
- Halaman simple karena semua info detail sudah ada di menu masing-masing

### content_5tahunan.md
- Persyaratan pembayaran pajak 5 tahunan
- Dokumen yang diperlukan untuk penggantian STNK dan plat nomor
- Prosedur dan langkah-langkah

### content_duplikat.md
- Syarat dan prosedur duplikat STNK hilang
- Dokumen yang diperlukan
- Langkah-langkah pengurusan

### content_mutasi.md
- Prosedur mutasi kendaraan masuk dan keluar daerah
- Persyaratan dokumen lengkap
- Langkah-langkah balik nama

### content_bbn.md
- BBN 1 (penyerahan pertama) untuk kendaraan baru
- BBN 2 (penyerahan kedua) untuk balik nama
- Persyaratan dokumen masing-masing

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
- ✅ Deployment config sudah disiapkan (autoscale)
- ✅ Aplikasi siap di-publish dengan klik tombol "Deploy"
- QR Code dapat di-generate dengan `python qr_generator.py` setelah website live
- QR Code bisa dicetak untuk poster/banner fisik agar pengunjung mudah akses website

## 🔐 Environment Variables
- `SESSION_SECRET`: Secret key untuk Flask session (sudah tersedia)
- `REPL_SLUG`: Otomatis dari Replit (untuk QR code URL)
- `REPL_OWNER`: Otomatis dari Replit (untuk QR code URL)

---

*Dokumentasi ini akan di-update seiring perkembangan proyek*
