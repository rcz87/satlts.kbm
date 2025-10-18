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
├── content_dasarhukum.md     # Konten dasar hukum dan peraturan
├── content_galery.md         # Konten galeri foto kegiatan SAMSAT
├── content_ikm.md            # Konten Indeks Kepuasan Masyarakat
├── qr_generator.py           # Script generator QR Code
├── templates/
│   └── index.html           # Template HTML dengan navigasi menu
├── static/
│   ├── style.css            # Styling CSS profesional dengan active state
│   ├── images/
│   │   ├── logo-samsat.png  # Logo resmi SAMSAT
│   │   └── galery/          # Folder untuk foto-foto kegiatan
│   └── documents/
│       ├── perpol-7-2021-regident.pdf  # Peraturan Kepolisian No. 7/2021
│       └── uu-22-2009-lalulintas.pdf   # UU No. 22/2009 Lalu Lintas
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
- 8 menu utama: Beranda, Syarat 5 Tahunan, Duplikat STNK, Mutasi Antar Daerah, BBN 1 & 2, Dasar Hukum, Galery, IKM
- Navigasi menu sticky dengan active state highlighting (golden border)
- Setiap halaman memuat konten Markdown yang spesifik
- Menu Dasar Hukum menampilkan daftar peraturan dengan PDF embedded viewer:
  - UU No. 22/2009 tentang Lalu Lintas dan Angkutan Jalan
  - Perpol No. 7/2021 tentang Regident Ranmor
  - Peraturan pendukung lainnya (PP 76/2020, UU 1/2022)
- Menu Galery untuk menampilkan foto-foto kegiatan pelayanan SAMSAT
- Menu IKM (Indeks Kepuasan Masyarakat) untuk survei kepuasan masyarakat

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

### 5. Halaman Dasar Hukum dengan PDF Viewer
- Halaman khusus untuk menampilkan berbagai peraturan perundangan
- Daftar peraturan: UU 22/2009, Perpol 7/2021, PP 76/2020, UU 1/2022
- Setiap peraturan bisa dibaca langsung (embedded PDF viewer) atau didownload
- Embedded PDF viewer menggunakan iframe untuk UU Lalu Lintas dan Perpol
- File PDF tersimpan di static/documents/
- Mudah untuk menambah peraturan baru di masa depan

### 6. Halaman Galeri Foto Kegiatan
- Halaman untuk menampilkan dokumentasi kegiatan pelayanan SAMSAT Kebumen
- Folder static/images/galery/ untuk menyimpan foto-foto kegiatan
- Placeholder konten yang informatif menjelaskan tujuan galeri
- Siap untuk diisi dengan foto-foto kegiatan seperti:
  - Pelayanan harian di loket
  - Kegiatan cek fisik kendaraan
  - Sosialisasi kepada masyarakat
  - Event dan kegiatan khusus
  - SAMSAT keliling
  - Layanan digital dan inovasi

### 7. Halaman Indeks Kepuasan Masyarakat (IKM)
- Halaman untuk survei kepuasan pelayanan publik
- Menjelaskan tujuan dan aspek penilaian IKM (9 aspek pelayanan)
- Placeholder untuk modul survei yang sedang dalam pengembangan
- Informasi lengkap tentang:
  - Tujuan IKM untuk peningkatan kualitas layanan
  - Aspek penilaian (persyaratan, prosedur, waktu, biaya, dll)
  - Fitur yang akan datang (formulir online, dashboard, grafik, dll)
- Masyarakat tetap bisa memberikan feedback via WhatsApp

## 📝 Recent Changes
- **18 Oktober 2025**: Tambah Menu Galery dan IKM
  - ✅ Tambahkan menu "📸 Galery" untuk dokumentasi foto kegiatan SAMSAT
  - ✅ Tambahkan menu "📊 IKM" (Indeks Kepuasan Masyarakat) untuk survei pelayanan
  - ✅ Buat file content_galery.md dengan placeholder konten untuk foto kegiatan
  - ✅ Buat file content_ikm.md dengan informasi lengkap tentang survei IKM
  - ✅ Buat folder static/images/galery/ untuk menyimpan foto-foto di masa depan
  - ✅ Routes baru: /galery dan /ikm
  - ✅ Total menu sekarang: 8 menu (Beranda, 5 Tahunan, Duplikat, Mutasi, BBN, Dasar Hukum, Galery, IKM)
  - ✅ Halaman IKM menjelaskan 9 aspek penilaian dan fitur survei yang akan datang
  - ✅ Siap untuk integrasi modul survei IKM di masa depan
- **18 Oktober 2025**: Ubah Menu Perpol 7/2021 menjadi Dasar Hukum
  - ✅ Ganti nama menu dari "Perpol 7/2021" menjadi "Dasar Hukum"
  - ✅ Tambahkan file UU No. 22/2009 tentang Lalu Lintas (420 KB PDF)
  - ✅ Buat halaman daftar peraturan dengan akses ke semua dokumen hukum
  - ✅ Setiap peraturan bisa dibaca online atau didownload PDF
  - ✅ Route baru: /dasarhukum, /lihat-uu-lalulintas, /lihat-perpol
  - ✅ Mudah menambah peraturan baru di masa depan
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
