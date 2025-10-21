# SAMSAT SMART INFOBOARD - Kebumen Edition

## Overview
SAMSAT SMART INFOBOARD - Kebumen Edition is a Flask-based web application providing the public with essential information regarding SAMSAT Kebumen services. It aims to streamline access to information on vehicle registration (STNK) and tax, operating hours, required documents, and estimated costs through a professional, user-friendly interface with QR code integration. This project serves as a foundational component for a larger vision: a comprehensive, interactive official website for Satlantas Polres Kebumen.

## User Preferences
- Bahasa Indonesia untuk semua konten dan komentar
- Styling profesional untuk kantor pemerintahan
- Emoji untuk visual appeal
- Responsive dan mobile-friendly

## System Architecture
The application is built with Flask, employing a multi-page architecture to deliver dynamic content rendered from Markdown files. It features a hierarchical menu structure based on Satlantas organizational divisions:

**Main Sections (5 Bidang Satlantas):**
1. **PELAYANAN REGIDENT** - Registrasi & Identifikasi Kendaraan
   - STNK & Pajak (Pajak 5 Tahunan, Duplikat STNK, Mutasi, BBN 1 & 2)
   - SIM (placeholder)
   - BPKB (placeholder)

2. **PELAYANAN GAKUM** - Penegakan Hukum Lalu Lintas
   - Unit Laka Lantas (placeholder)
   - Tilang & ETLE (placeholder)

3. **PATWAL** - Patroli & Pengawalan (placeholder)
4. **KAMSEL** - Keamanan & Keselamatan (placeholder)
5. **URMIN** - Urusan Dalam & Administrasi (placeholder)

**Additional Menus:**
- IKM (Indeks Kepuasan Masyarakat) - Fully functional survey system
- Dasar Hukum - Legal documents with PDF viewer
- Gallery - Photo documentation

The UI/UX is designed professionally with a blue gradient header, responsive navigation, and print-friendly styling. A fully integrated IKM survey system allows users to rate services with a star system and comments, displaying results on a real-time dashboard based on 9 criteria and categorized according to Permenpan RB No. 14/2017. Security features include CSRF protection, rate limiting (IKM: 50 per day, Feedback: 20 per hour), comprehensive security headers, input validation, and secure session management, aligning with OWASP Top 10 and BSSN standards.

## Recent Changes (October 2025)
- **Homepage Content Separation (21 Okt 2025)**: Separated homepage into Satlantas profile (Sambutan Kasat Lantas, Tupoksi, Visi-Misi, Struktur Organisasi) and SAMSAT-specific content moved to /regident/stnk page. Updated header address to Jl. Pahlawan No. 40 (Satlantas HQ) from Jl. Tentara Pelajar No. 54 (SAMSAT office).
- **Menu Restructure (Oktober 2025)**: Complete website restructure based on Satlantas organizational divisions (REGIDENT, GAKUM, PATWAL, KAMSEL, URMIN) with hierarchical navigation - Phase 1 complete with placeholder content ready for future expansion
- **BBN II Fee Update**: Removed BPNKB 10% charge from BBN II (second-hand vehicle transfer) per new 2025 regulation - now only PKB + OPSEN + admin fees, resulting in massive savings (motor: Rp 1-2M, mobil: Rp 10-20M)
- **IKM Rate Limit Adjustment**: Increased from 10 per hour to 50 per day to accommodate public survey participation from shared networks
- **Mutasi Processing Time**: Updated from 1-2 days to 4-5 working days based on real operational data
- **Favicon Added**: Professional logo-samsat.png as website favicon

## External Dependencies
- **Backend Framework**: Flask (Python 3.11)
- **Database**: PostgreSQL (Neon) for IKM survey data
- **Templating Engine**: Jinja2
- **Markdown Parser**: python-markdown
- **QR Code Generation**: qrcode + Pillow
- **Frontend Interactivity**: Vanilla JavaScript
- **Security**: Flask-WTF (CSRF protection), Flask-Limiter (rate limiting)

## Blueprint: Portal Layanan Digital Satlantas Polres Kebumen
**Status Aplikasi Saat Ini:** Foundational Component / MVP Phase 0 (SELESAI 100%)

### Visi Besar (6-Month Roadmap)
Mengembangkan **Portal Layanan Digital Satlantas Polres Kebumen** yang komprehensif dengan kepatuhan penuh terhadap regulasi E-Government Indonesia (KIP, BSSN Level 2, WCAG Accessibility).

### Pilar Kepatuhan Regulasi (WAJIB)
1. **Keterbukaan Informasi Publik (KIP)** - UU No. 14/2008, Perki No. 1/2010
   - Konten wajib: Tupoksi, Visi/Misi, Struktur Organisasi, Biodata Pimpinan, Renja SKPD, Ringkasan Anggaran, Peraturan
   - Frekuensi update: Berkala (semester/tahun), Serta Merta (real-time), Tersedia Setiap Saat
   - CMS dengan search engine fungsional
2. **Keamanan Siber BSSN Level 2** - Minimal Implementation Level
   - SSL/TLS Certificate
   - Web Application Firewall
   - Audit keamanan berkala
   - Pengelolaan identitas dan otentikasi
3. **Aksesibilitas WCAG** - Permen PAN-RB No. 11/2024
   - Perceivable: Alt text, kontras warna, caption video
   - Operable: Keyboard navigation, waktu sesi fleksibel
   - Understandable: Bahasa lugas, navigasi konsisten
   - Robust: Kompatibel dengan screen readers

### Arsitektur Menu Portal (Target)
```
Beranda (Homepage)
├─ Quick Access Buttons (Prioritas):
│  1. Cek Tilang ETLE
│  2. Perpanjangan SIM (SINAR)
│  3. Cek Samsat Digital (SIGNAL)
│  4. Kontak Darurat Satlantas
│  5. Peta Lokasi Layanan
│
Profil Satlantas
├─ Sejarah
├─ Visi, Misi, Moto
├─ Tupoksi (Tugas Pokok dan Fungsi)
├─ Struktur Organisasi
├─ Biodata Pimpinan & SDM
│
Layanan Publik (Gateway Integration)
├─ SIM (SINAR) - Panduan + Deep Link
├─ Tilang (ETLE) - Prosedur Merah/Biru
├─ STNK & Pajak (SIGNAL) - Jadwal Samling
├─ Panduan Lokal Kebumen:
│  ├─ Lokasi SATPAS untuk Ujian Praktik
│  ├─ Mitra RIKKES & Psikologi (biaya ~Rp 37.500)
│  └─ Prosedur Tilang di SPKT Polres Kebumen
│
Informasi KIP
├─ Renja SKPD (Rencana Kerja)
├─ Renstra SKPD (Rencana Strategis)
├─ Ringkasan Anggaran Program/Kegiatan
├─ Peraturan & Kebijakan Lalu Lintas
├─ Dokumen Resmi (downloadable)
│
Berita & Pengumuman
├─ Berita Terkini (sumber internal Satlantas)
├─ Pengumuman Operasi/Razia
├─ Info Serta Merta (penutupan jalan, bencana)
├─ Dokumentasi Kegiatan (foto/video)
│
Kontak & Lokasi
├─ Nomor Darurat: 0287-385514 (Satlantas)
├─ Nomor Umum: 0287-382110 (Polres)
├─ Jam Operasional: Senin-Kamis 09:00-16:00
├─ 4 Lokasi Samsat Kebumen (Peta Interaktif):
│  ├─ Jl. Tentara Pelajar No.54, Panjer
│  ├─ Klapasawit, Wero, Gombong
│  ├─ Jl. Indrakila, Kebumen
│  └─ Kantor Kecamatan Ayah, Demangsari
├─ Nomor Penting Lainnya (Damkar, RSUD, PMI)
```

### Integrasi Platform Digital Nasional (Korlantas POLRI)
| Platform | Layanan | Fungsi di Website Kebumen | Data Lokal yang Disediakan |
|----------|---------|---------------------------|---------------------------|
| **SINAR** | SIM Online | Deep link + Panduan persyaratan | Lokasi SATPAS, Mitra RIKKES/Psikologi Kebumen |
| **ETLE** | Tilang Elektronik | Link cek tilang + Prosedur | Jam SPKT, Prosedur Tilang Merah/Biru |
| **SIGNAL** | Samsat Digital | Link pembayaran pajak | Jadwal & Lokasi Samsat Keliling |

### Homepage Design Blueprint (5 Zona Strategis)
1. **Header & Navigasi**: Logo, Nama Instansi, Menu Utama, Search Box
2. **Hero Section**: Visi/Moto Satlantas (ringkas, visual)
3. **Quick Access Buttons**: 5 tombol prioritas (ETLE, SINAR, SIGNAL, Kontak, Peta)
4. **Zona Informasi**: Berita Terkini, Pengumuman, Link KIP
5. **Footer**: Widget aksesibilitas (kontras, ukuran font), Link App Store, Sitemap

### Roadmap Implementasi (6 Bulan)
**Fase I (Bulan 1) - Perencanaan & Legalitas**
- Pembentukan Tim Pengelola Situs Web
- Pengajuan domain .go.id (satlantas.polreskebumen.go.id)
- Audit konten KIP dan spesifikasi BSSN
- Output: Dokumen perencanaan, Spesifikasi teknis

**Fase II (Bulan 2-3) - Desain & Infrastruktur**
- Implementasi CMS profesional (template-based)
- Development struktur navigasi & homepage blueprint
- Search engine fungsional
- Output: Website Beta, mesin pencari

**Fase III (Bulan 4-5) - Konten & Integrasi**
- Upload konten KIP wajib (Tupoksi, Renja, Anggaran)
- Integrasi deep links SINAR/ETLE/SIGNAL
- Input data lokal (jadwal Samling, mitra RIKKES)
- Output: Konten minimal terpenuhi, tautan teruji

**Fase IV (Bulan 6) - Uji Publik & Go Live**
- Penetration testing (validasi BSSN Level 2)
- WCAG testing (keyboard nav, kontras, screen reader)
- Peluncuran resmi
- Output: Portal live dengan kepatuhan penuh

### Status Komponen yang Sudah Ada
✅ **SAMSAT Smart Infoboard (MVP/Phase 0)** - Sudah Selesai:
- Informasi layanan SAMSAT lengkap (Pajak 5 Tahunan, Duplikat STNK, Mutasi, BBN I & II)
- IKM Survey System (9 kriteria, database PostgreSQL, rate limit 50/day)
- Feedback System (rate limit 20/hour)
- Gallery & Dasar Hukum (PDF viewer)
- Security: CSRF, rate limiting, secure headers
- Professional UI/UX dengan blue gradient

### Komponen yang Belum Dibangun
❌ **Untuk Mencapai Portal Lengkap:**
- Profil kelembagaan (Tupoksi, Struktur, Biodata Pimpinan)
- Integrasi SINAR/ETLE/SIGNAL (deep links + panduan lokal)
- Konten KIP wajib (Renja SKPD, Ringkasan Anggaran, Renstra)
- CMS profesional dengan search engine
- Berita & Pengumuman real-time
- WCAG compliance (keyboard nav, screen reader, aksesibilitas widget)
- Peta lokasi interaktif (Google Maps embedded)
- Domain resmi .go.id

### Referensi Dokumen Blueprint
File: `attached_assets/Riset web_1761014386025.txt` (148 baris)
- Laporan Ahli: Cetak Biru Arsitektur Portal Satlantas Polres Kebumen
- Mencakup: Kepatuhan E-Gov, Integrasi SINAR-ETLE-SIGNAL, Aksesibilitas WCAG
- Standar: UU KIP No. 14/2008, BSSN Level 2, Permen PAN-RB No. 11/2024