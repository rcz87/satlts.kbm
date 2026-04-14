# 🔐 Panduan Sistem Admin Portal Satlantas

## 📋 Overview
Sistem admin telah berhasil dibangun untuk Portal Satlantas Polres Kebumen dengan fitur lengkap untuk mengelola konten, monitoring IKM, dan moderasi feedback.

## 🎯 Fitur Sistem Admin

### 1. **Autentikasi & Keamanan**
- ✅ Login page dengan password hashing (scrypt algorithm)
- ✅ CSRF Protection untuk semua form
- ✅ Rate limiting login (10 attempts per hour)
- ✅ Session management yang aman
- ✅ Login required decorator untuk semua halaman admin

### 2. **Dashboard Admin** (`/admin/dashboard`)
- ✅ Statistik real-time:
  - Total responden IKM
  - Total feedback masuk
  - Rata-rata skor IKM
- ✅ Chart data IKM 7 hari terakhir
- ✅ Komentar IKM terbaru
- ✅ Feedback terbaru

### 3. **Manajemen IKM** (`/admin/ikm`)
- ✅ Daftar semua responden dengan pagination
- ✅ Detail lengkap setiap responden:
  - 9 kriteria penilaian
  - Skor total dan kategori (A/B/C/D)
  - Komentar dan saran
- ✅ Filter dan sorting
- ✅ View history berdasarkan waktu

### 4. **Manajemen Feedback** (`/admin/feedback`)
- ✅ Daftar semua feedback dengan pagination
- ✅ Moderasi: hapus feedback tidak relevan
- ✅ View detail pesan lengkap

### 5. **Manajemen Gallery** (`/admin/gallery`)
- ✅ Upload foto baru (JPG, JPEG, PNG)
- ✅ Preview semua foto
- ✅ Delete foto yang tidak diperlukan
- ✅ Automatic timestamping untuk nama file

### 6. **Manajemen Dokumen** (`/admin/documents`)
- ✅ Upload dokumen PDF
- ✅ Daftar semua dokumen
- ✅ Delete dokumen
- ✅ Link langsung ke PDF viewer

## 🔑 Bootstrap Admin Pertama

Setelah fresh deploy, database admin kosong. Buat admin pertama dengan script:

```bash
# Interaktif (akan minta username, nama, password)
python create_admin.py

# Non-interaktif (untuk CI/deploy otomatis)
ADMIN_PASSWORD='password_kuat_minimal_8_char' python create_admin.py admin "Admin Satlantas"
```

**PENTING:**
- Password minimal 8 karakter
- Jangan pakai password default/lemah di production
- Jalankan sekali saja saat setup awal

## 📱 Akses Admin Panel

1. **Buka halaman login:**
   ```
   https://your-domain.com/admin/login
   ```

2. **Login dengan kredensial default**

3. **Navigasi menu admin:**
   - 📊 Dashboard - Overview statistik
   - 📋 IKM - Data survei kepuasan masyarakat
   - 💬 Feedback - Pesan dan saran masyarakat
   - 🖼️ Gallery - Kelola foto dokumentasi
   - 📄 Dokumen - Kelola file PDF
   - 🌐 Lihat Website - Preview website publik

## 🗄️ Database Schema

### Tabel: `admin_users`
```sql
CREATE TABLE admin_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);
```

## 🔒 Fitur Keamanan

### Authentication
- Password hashing menggunakan Werkzeug scrypt
- Session-based authentication
- Auto logout setelah inactive

### CSRF Protection
- Semua form dilindungi CSRF token
- Validasi token otomatis

### Rate Limiting
- Login: 10 attempts per hour per IP
- Mencegah brute force attacks

### Input Validation
- File upload hanya accept format yang ditentukan
- Secure filename untuk mencegah path traversal
- Input sanitization untuk semua form

## 📝 Cara Menambah Admin Baru

Jalankan SQL berikut di database console:

```sql
-- 1. Generate password hash terlebih dahulu dengan Python:
-- python3 -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('password_anda'))"

-- 2. Insert admin baru:
INSERT INTO admin_users (username, password_hash, full_name, is_active) 
VALUES (
    'username_baru',
    'scrypt:32768:8:1$...',  -- ganti dengan hash dari step 1
    'Nama Lengkap Admin',
    TRUE
);
```

## 🎨 Struktur File

```
portal-satlantas/
├── app_admin.py                    # Admin blueprint & routes
├── templates/admin/
│   ├── base.html                   # Base template admin
│   ├── login.html                  # Halaman login
│   ├── dashboard.html              # Dashboard utama
│   ├── ikm_list.html              # Daftar IKM
│   ├── ikm_detail.html            # Detail IKM
│   ├── feedback_list.html         # Daftar feedback
│   ├── gallery.html               # Manajemen gallery
│   └── documents.html             # Manajemen dokumen
└── static/
    ├── images/galery/             # Foto gallery
    └── documents/                 # File PDF
```

## 🚀 Deployment Notes

### Production Environment
Untuk production di VPS Hostinger, pastikan:

1. **Ganti SESSION_SECRET:**
   ```bash
   # Di .env file
   SESSION_SECRET=random-secret-key-yang-panjang-dan-aman
   ```

2. **Secure cookies sudah aktif:**
   - HTTPS wajib diaktifkan
   - SESSION_COOKIE_SECURE = True (sudah diset otomatis jika not debug)

3. **Backup database regular:**
   ```bash
   # Gunakan script backup yang sudah tersedia
   ./deploy/backup-db.sh
   ```

4. **Monitor logs:**
   ```bash
   # Production logs
   tail -f logs/satlantas.log
   ```

## 📊 Kategori IKM

Berdasarkan Permenpan RB No. 14/2017:

| Skor | Kategori | Keterangan |
|------|----------|------------|
| 88.31 - 100 | A | Sangat Baik |
| 76.61 - 88.30 | B | Baik |
| 65.00 - 76.60 | C | Kurang Baik |
| < 65.00 | D | Tidak Baik |

## 🛡️ Best Practices

### Keamanan
1. ✅ Ganti password default segera
2. ✅ Gunakan password yang kuat (min 12 karakter)
3. ✅ Logout setelah selesai
4. ✅ Jangan share kredensial admin
5. ✅ Monitor aktivitas login (check last_login)

### Manajemen Konten
1. ✅ Backup foto/dokumen sebelum delete
2. ✅ Gunakan nama file yang deskriptif
3. ✅ Compress foto sebelum upload (max 2MB recommended)
4. ✅ Regular cleanup foto/dokumen yang tidak terpakai

### Monitoring
1. ✅ Check dashboard minimal 1x sehari
2. ✅ Respond komentar IKM yang membutuhkan tindakan
3. ✅ Moderasi feedback yang masuk
4. ✅ Export data IKM regular untuk laporan

## 🔧 Troubleshooting

### Login Gagal
- Pastikan username/password benar
- Check rate limit (max 10 attempts per hour)
- Clear browser cache & cookies

### Upload File Gagal
- Check ukuran file (max 16MB default Flask)
- Pastikan format file sesuai (JPG/PNG untuk foto, PDF untuk dokumen)
- Check permission folder static/images/galery dan static/documents

### Data Tidak Muncul
- Refresh browser (Ctrl+F5)
- Check database connection
- Review logs: `logs/satlantas.log`

## 📞 Support

Untuk bantuan teknis, hubungi developer atau check:
- Documentation: `/DEPLOYMENT.md`
- Project info: `/replit.md`
- Logs: `/logs/satlantas.log`

---

**Last Updated:** 27 Oktober 2025
**Version:** 1.0.0
**Status:** Production Ready ✅
