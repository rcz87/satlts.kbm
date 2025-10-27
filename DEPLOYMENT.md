# 🚀 PANDUAN DEPLOYMENT PRODUCTION
# Portal Satlantas Polres Kebumen - Hostinger VPS

---

## 📋 Daftar Isi

1. [Persiapan](#1-persiapan)
2. [Setup VPS Hostinger](#2-setup-vps-hostinger)
3. [Install Dependencies](#3-install-dependencies)
4. [Setup Database PostgreSQL](#4-setup-database-postgresql)
5. [Deploy Aplikasi](#5-deploy-aplikasi)
6. [Konfigurasi Nginx](#6-konfigurasi-nginx)
7. [Setup Systemd Service](#7-setup-systemd-service)
8. [Install SSL Certificate](#8-install-ssl-certificate)
9. [Setup Backup Otomatis](#9-setup-backup-otomatis)
10. [Maintenance & Update](#10-maintenance--update)
11. [Troubleshooting](#11-troubleshooting)

---

## 1. Persiapan

### ✅ Checklist Sebelum Mulai

- [ ] VPS Hostinger sudah aktif (minimum: KVM 1 - 2GB RAM, 1 CPU)
- [ ] Akses SSH ke VPS (username & password dari hPanel)
- [ ] Domain sudah siap (contoh: `satlantas.polreskebumen.go.id`)
- [ ] DNS domain sudah diarahkan ke IP VPS
- [ ] Source code aplikasi sudah siap (download dari Replit atau Git)

### 📦 Spesifikasi VPS yang Direkomendasikan

**Minimum (untuk testing):**
- **Plan:** KVM 1
- **RAM:** 2 GB
- **CPU:** 1 Core
- **Storage:** 50 GB NVMe SSD
- **Estimasi:** Rp 69.000/bulan

**Recommended (untuk production):**
- **Plan:** KVM 2 (Best Seller)
- **RAM:** 8 GB
- **CPU:** 2 Cores
- **Storage:** 100 GB NVMe SSD
- **Estimasi:** Rp 129.000/bulan

### 🌐 Setup Domain di hPanel Hostinger

1. Login ke [hPanel Hostinger](https://hpanel.hostinger.com)
2. Pilih **VPS** dari menu utama
3. Klik VPS Anda → **Overview** → Catat **IP Address**
4. Ke menu **Domains** → Pilih domain Anda
5. Klik **DNS Zone**
6. Tambah/Edit record:
   - **Type:** A
   - **Name:** @ (untuk root domain) atau www
   - **Points to:** [IP Address VPS Anda]
   - **TTL:** 14400 (4 hours)
7. Save dan tunggu propagasi DNS (5-60 menit)

---

## 2. Setup VPS Hostinger

### 2.1. Pilih Operating System

1. Login ke **hPanel** → **VPS** → Pilih server Anda
2. Klik **OS & Panel** → **Operating System**
3. Pilih **Plain OS** → **Ubuntu 22.04 64bit** atau **Ubuntu 24.04 64bit**
4. Klik **Change OS** (⚠️ Ini akan menghapus semua data)
5. Tunggu instalasi selesai (~5-10 menit)

### 2.2. Koneksi SSH ke VPS

Dari hPanel, di bagian **Overview**, Anda akan melihat:
- **SSH Access:** `ssh root@xxx.xxx.xxx.xxx -p 22`
- **Password:** [Ditampilkan di hPanel]

**Windows (PowerShell atau PuTTY):**
```bash
ssh root@YOUR_VPS_IP
# Masukkan password saat diminta
```

**Linux/Mac (Terminal):**
```bash
ssh root@YOUR_VPS_IP
# Masukkan password saat diminta
```

### 2.3. Update System & Setup User

```bash
# Update package list
sudo apt update && sudo apt upgrade -y

# Install essential tools
sudo apt install -y git curl wget vim ufw software-properties-common

# Buat user baru (ganti 'satlantas' dengan username pilihan Anda)
adduser satlantas
# Ikuti prompt: masukkan password, dan informasi lainnya

# Tambahkan user ke grup sudo
usermod -aG sudo satlantas

# Tambahkan user ke grup www-data (untuk Nginx)
usermod -aG www-data satlantas

# Switch ke user baru
su - satlantas
```

### 2.4. Setup Firewall (UFW)

```bash
# Enable firewall
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable

# Check status
sudo ufw status
```

---

## 3. Install Dependencies

### 3.1. Install Python 3.11

```bash
# Install Python 3.11
sudo apt install -y python3.11 python3.11-venv python3.11-dev

# Install pip
sudo apt install -y python3-pip

# Verifikasi instalasi
python3.11 --version
pip3 --version
```

### 3.2. Install PostgreSQL

```bash
# Install PostgreSQL
sudo apt install -y postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Check status
sudo systemctl status postgresql
```

### 3.3. Install Nginx

```bash
# Install Nginx
sudo apt install -y nginx

# Start Nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx
```

### 3.4. Install Certbot (untuk SSL)

```bash
# Install Certbot untuk Let's Encrypt SSL
sudo apt install -y certbot python3-certbot-nginx
```

---

## 4. Setup Database PostgreSQL

### 4.1. Buat User & Database

```bash
# Login ke PostgreSQL sebagai user postgres
sudo -u postgres psql

# Jalankan command SQL berikut:
```

```sql
-- Buat user database (ganti 'password123' dengan password yang kuat)
CREATE USER satlantas WITH PASSWORD 'password123';

-- Buat database
CREATE DATABASE satlantas_db;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE satlantas_db TO satlantas;

-- Exit
\q
```

### 4.2. Buat Tabel IKM Survey

```bash
# Login ke database sebagai user satlantas
psql -U satlantas -d satlantas_db -h localhost

# Jalankan SQL berikut untuk membuat tabel:
```

```sql
CREATE TABLE ikm_responses (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255),
    pelayanan_1 INTEGER CHECK (pelayanan_1 BETWEEN 1 AND 5),
    pelayanan_2 INTEGER CHECK (pelayanan_2 BETWEEN 1 AND 5),
    pelayanan_3 INTEGER CHECK (pelayanan_3 BETWEEN 1 AND 5),
    pelayanan_4 INTEGER CHECK (pelayanan_4 BETWEEN 1 AND 5),
    pelayanan_5 INTEGER CHECK (pelayanan_5 BETWEEN 1 AND 5),
    pelayanan_6 INTEGER CHECK (pelayanan_6 BETWEEN 1 AND 5),
    pelayanan_7 INTEGER CHECK (pelayanan_7 BETWEEN 1 AND 5),
    pelayanan_8 INTEGER CHECK (pelayanan_8 BETWEEN 1 AND 5),
    pelayanan_9 INTEGER CHECK (pelayanan_9 BETWEEN 1 AND 5),
    comments TEXT
);

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255),
    email VARCHAR(255),
    subject VARCHAR(500),
    message TEXT
);

-- Verifikasi tabel sudah dibuat
\dt

-- Exit
\q
```

### 4.3. Test Koneksi Database

```bash
# Test koneksi
psql -U satlantas -d satlantas_db -h localhost -c "SELECT version();"
```

---

## 5. Deploy Aplikasi

### 5.1. Upload Source Code ke VPS

**Opsi A: Upload via Git (Recommended)**
```bash
# Pindah ke home directory
cd ~

# Clone repository (jika menggunakan Git)
git clone https://github.com/YOUR_USERNAME/portal-satlantas.git
cd portal-satlantas

# Atau buat folder dan upload manual
mkdir -p ~/portal-satlantas
cd ~/portal-satlantas
```

**Opsi B: Upload via SCP (dari komputer lokal)**
```bash
# Dari komputer lokal (bukan di VPS)
scp -r /path/to/portal-satlantas satlantas@YOUR_VPS_IP:~/
```

**Opsi C: Download ZIP dari Replit**
```bash
# Di VPS, download source code
wget https://replit.com/@yourusername/portal-satlantas/download -O portal.zip
unzip portal.zip -d ~/portal-satlantas
cd ~/portal-satlantas
```

### 5.2. Setup Directory Structure

```bash
# Pindahkan aplikasi ke /var/www
sudo mkdir -p /var/www/satlantas
sudo cp -r ~/portal-satlantas/* /var/www/satlantas/
sudo chown -R satlantas:www-data /var/www/satlantas
sudo chmod 755 /var/www/satlantas
```

### 5.3. Setup Virtual Environment

```bash
# Pindah ke directory aplikasi
cd /var/www/satlantas

# Buat virtual environment
python3.11 -m venv venv

# Aktifkan virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verifikasi instalasi
pip list
```

### 5.4. Setup Environment Variables

```bash
# Copy .env.example menjadi .env
cp .env.example .env

# Edit .env dan isi dengan nilai sebenarnya
nano .env
```

**Isi file `.env`:**
```bash
# Database Configuration
DATABASE_URL=postgresql://satlantas:password123@localhost:5432/satlantas_db
PGHOST=localhost
PGPORT=5432
PGUSER=satlantas
PGPASSWORD=password123
PGDATABASE=satlantas_db

# Flask Secret Key (generate random string!)
# Generate dengan: python3 -c "import secrets; print(secrets.token_hex(32))"
SESSION_SECRET=generated-random-secret-key-disini-min-32-karakter

# Flask Configuration
FLASK_ENV=production
FLASK_DEBUG=False
```

**Generate SESSION_SECRET:**
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
# Copy output dan paste ke .env
```

### 5.5. Buat Folder Logs

```bash
# Buat folder logs untuk aplikasi
sudo mkdir -p /var/log/satlantas
sudo chown satlantas:www-data /var/log/satlantas
sudo chmod 755 /var/log/satlantas

# Buat folder logs di aplikasi
cd /var/www/satlantas
mkdir -p logs
```

### 5.6. Test Aplikasi dengan Gunicorn

```bash
# Aktifkan virtual environment (jika belum)
cd /var/www/satlantas
source venv/bin/activate

# Test run dengan Gunicorn
gunicorn --bind 0.0.0.0:8000 wsgi:app

# Buka browser dan akses: http://YOUR_VPS_IP:8000
# Jika berhasil, tekan Ctrl+C untuk stop
```

---

## 6. Konfigurasi Nginx

### 6.1. Copy & Edit Nginx Config

```bash
# Copy file konfigurasi Nginx
sudo cp /var/www/satlantas/deploy/hostinger-nginx.conf /etc/nginx/sites-available/satlantas

# Edit konfigurasi
sudo nano /etc/nginx/sites-available/satlantas
```

**Ubah bagian berikut:**
1. Ganti `YOUR_DOMAIN` dengan domain Anda (contoh: `satlantas.polreskebumen.go.id`)
2. Pastikan path `/var/www/satlantas` sesuai

### 6.2. Enable Site

```bash
# Buat symbolic link ke sites-enabled
sudo ln -s /etc/nginx/sites-available/satlantas /etc/nginx/sites-enabled/

# Hapus default site (optional)
sudo rm /etc/nginx/sites-enabled/default

# Test konfigurasi Nginx
sudo nginx -t

# Jika OK, reload Nginx
sudo systemctl reload nginx
```

---

## 7. Setup Systemd Service

### 7.1. Copy & Edit Service File

```bash
# Copy systemd service file
sudo cp /var/www/satlantas/deploy/satlantas.service /etc/systemd/system/

# Edit service file
sudo nano /etc/systemd/system/satlantas.service
```

**Pastikan path dan username sudah benar:**
- `User=satlantas` (username VPS Anda)
- `WorkingDirectory=/var/www/satlantas`
- `Environment="PATH=/var/www/satlantas/venv/bin"`
- `EnvironmentFile=/var/www/satlantas/.env`

### 7.2. Start & Enable Service

```bash
# Reload systemd daemon
sudo systemctl daemon-reload

# Start service
sudo systemctl start satlantas

# Check status
sudo systemctl status satlantas

# Jika berjalan dengan baik, enable auto-start on boot
sudo systemctl enable satlantas

# Restart Nginx
sudo systemctl restart nginx
```

### 7.3. Test Aplikasi

Buka browser dan akses:
- `http://YOUR_DOMAIN` atau
- `http://YOUR_VPS_IP`

Anda seharusnya melihat **Portal Satlantas Polres Kebumen** berjalan!

---

## 8. Install SSL Certificate

### 8.1. Obtain SSL Certificate dengan Let's Encrypt

```bash
# Jalankan Certbot
sudo certbot --nginx -d satlantas.polreskebumen.go.id -d www.satlantas.polreskebumen.go.id

# Ikuti prompt:
# - Masukkan email untuk notifikasi
# - Setuju Terms of Service (Y)
# - Redirect HTTP ke HTTPS? (2 - Yes, recommended)
```

### 8.2. Test Auto-renewal

```bash
# Test automatic renewal
sudo certbot renew --dry-run

# Jika berhasil, certificate akan auto-renew setiap 90 hari
```

### 8.3. Verifikasi HTTPS

Akses: `https://satlantas.polreskebumen.go.id`

Pastikan:
- ✅ Gembok hijau muncul di browser
- ✅ Certificate valid
- ✅ HTTP auto-redirect ke HTTPS

---

## 9. Setup Backup Otomatis

### 9.1. Setup Backup Script

```bash
# Copy backup script
sudo cp /var/www/satlantas/deploy/backup-db.sh /opt/scripts/
sudo chmod +x /opt/scripts/backup-db.sh

# Buat folder backup
sudo mkdir -p /var/backups/satlantas
sudo chown satlantas:satlantas /var/backups/satlantas

# Test manual backup
/opt/scripts/backup-db.sh
```

### 9.2. Setup Cron Job untuk Auto Backup

```bash
# Edit crontab
crontab -e

# Pilih editor (nano), lalu tambahkan di bagian bawah:
# Backup setiap hari jam 2 pagi
0 2 * * * /opt/scripts/backup-db.sh >> /var/log/satlantas/backup.log 2>&1

# Save dan exit (Ctrl+X, Y, Enter)
```

### 9.3. Verifikasi Cron Job

```bash
# List cron jobs
crontab -l

# Check backup log
tail -f /var/log/satlantas/backup.log
```

---

## 10. Maintenance & Update

### 10.1. Update Aplikasi

```bash
# 1. Backup database terlebih dahulu
/opt/scripts/backup-db.sh

# 2. Pull latest code (jika menggunakan Git)
cd /var/www/satlantas
git pull origin main

# Atau upload file baru via SCP

# 3. Aktifkan virtual environment
source venv/bin/activate

# 4. Update dependencies (jika ada perubahan)
pip install -r requirements.txt

# 5. Restart aplikasi
sudo systemctl restart satlantas

# 6. Check status
sudo systemctl status satlantas

# 7. Check logs
sudo journalctl -u satlantas -n 50
```

### 10.2. Monitor Logs

```bash
# Application logs (real-time)
sudo journalctl -u satlantas -f

# Nginx access log
sudo tail -f /var/log/nginx/satlantas-access.log

# Nginx error log
sudo tail -f /var/log/nginx/satlantas-error.log

# Application error log
tail -f /var/www/satlantas/logs/satlantas.log
```

### 10.3. Restart Services

```bash
# Restart aplikasi Flask
sudo systemctl restart satlantas

# Reload Nginx (no downtime)
sudo systemctl reload nginx

# Restart Nginx
sudo systemctl restart nginx

# Restart PostgreSQL
sudo systemctl restart postgresql
```

---

## 11. Troubleshooting

### 🔴 502 Bad Gateway

**Penyebab:**
- Gunicorn service tidak berjalan
- Socket file tidak ada

**Solusi:**
```bash
# Check service status
sudo systemctl status satlantas

# Check logs
sudo journalctl -u satlantas -n 100

# Restart service
sudo systemctl restart satlantas

# Check socket file exists
ls -la /var/www/satlantas/satlantas.sock
```

### 🔴 500 Internal Server Error

**Penyebab:**
- Error di aplikasi Flask
- Database connection error
- Missing environment variables

**Solusi:**
```bash
# Check application logs
tail -f /var/www/satlantas/logs/satlantas.log
sudo journalctl -u satlantas -n 100

# Test database connection
psql -U satlantas -d satlantas_db -h localhost -c "SELECT 1;"

# Verify .env file
cat /var/www/satlantas/.env

# Test aplikasi manual
cd /var/www/satlantas
source venv/bin/activate
python wsgi.py
```

### 🔴 Permission Denied on Socket

**Solusi:**
```bash
# Add user to www-data group
sudo usermod -aG www-data satlantas

# Fix directory permissions
sudo chown -R satlantas:www-data /var/www/satlantas
sudo chmod 755 /var/www/satlantas

# Restart service
sudo systemctl restart satlantas
```

### 🔴 Static Files Not Loading

**Solusi:**
```bash
# Check static files directory
ls -la /var/www/satlantas/static/

# Fix permissions
sudo chown -R satlantas:www-data /var/www/satlantas/static
sudo chmod -R 755 /var/www/satlantas/static

# Check Nginx config
sudo nginx -t
sudo systemctl reload nginx
```

### 🔴 Database Connection Error

**Solusi:**
```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Test connection
psql -U satlantas -d satlantas_db -h localhost

# Check .env DATABASE_URL
cat /var/www/satlantas/.env | grep DATABASE_URL

# Restart PostgreSQL
sudo systemctl restart postgresql
```

### 🔴 Service Won't Start

**Solusi:**
```bash
# Check detailed logs
sudo journalctl -u satlantas -xe

# Test Gunicorn manually
cd /var/www/satlantas
source venv/bin/activate
gunicorn --bind 0.0.0.0:8000 wsgi:app

# Check service file syntax
sudo systemctl cat satlantas

# Reload daemon and restart
sudo systemctl daemon-reload
sudo systemctl restart satlantas
```

---

## 📊 Performance Monitoring

### Resource Usage

```bash
# Check system resources
htop

# Check disk usage
df -h

# Check memory usage
free -h

# Check PostgreSQL connections
sudo -u postgres psql -c "SELECT count(*) FROM pg_stat_activity;"
```

### Optimize Performance

**Gunicorn Workers:**
```bash
# Edit service file
sudo nano /etc/systemd/system/satlantas.service

# Adjust workers based on CPU cores
# Formula: (2 x CPU_cores) + 1
# 1 CPU: --workers 3
# 2 CPU: --workers 5
# 4 CPU: --workers 9

sudo systemctl daemon-reload
sudo systemctl restart satlantas
```

---

## 🎯 Checklist Production-Ready

- [ ] ✅ VPS setup dengan Ubuntu 22.04/24.04
- [ ] ✅ Firewall (UFW) enabled
- [ ] ✅ Non-root user untuk aplikasi
- [ ] ✅ PostgreSQL database setup
- [ ] ✅ Environment variables configured (.env)
- [ ] ✅ Gunicorn service running
- [ ] ✅ Nginx configured dan running
- [ ] ✅ SSL Certificate installed (HTTPS)
- [ ] ✅ Domain DNS pointing ke VPS
- [ ] ✅ Backup otomatis (cron job)
- [ ] ✅ Logs monitoring setup
- [ ] ✅ Application tested dan berjalan
- [ ] ✅ Security headers enabled
- [ ] ✅ Rate limiting active
- [ ] ✅ CSRF protection enabled

---

## 📞 Support & Resources

### Hostinger VPS Support
- **Knowledge Base:** https://support.hostinger.com/
- **Live Chat:** Available di hPanel (24/7)
- **Ticket Support:** submit@hostinger.com

### Dokumentasi Teknis
- **Flask Deployment:** https://flask.palletsprojects.com/en/stable/deploying/
- **Gunicorn Docs:** https://docs.gunicorn.org/
- **Nginx Docs:** https://nginx.org/en/docs/
- **PostgreSQL Docs:** https://www.postgresql.org/docs/

---

## 🎉 Selamat!

Aplikasi **Portal Satlantas Polres Kebumen** Anda sekarang sudah berjalan di production di VPS Hostinger dengan konfigurasi yang aman dan professional!

Langkah selanjutnya:
1. ✅ Monitor performa dan logs secara berkala
2. ✅ Setup monitoring tools (optional: Uptime Robot, Pingdom)
3. ✅ Lakukan regular backup dan test restore
4. ✅ Keep system dan dependencies up to date
5. ✅ Daftar PSE Kominfo untuk compliance
6. ✅ Audit keamanan BSSN Level 2
7. ✅ WCAG accessibility testing

**Semoga sukses dengan portal resmi Satlantas Polres Kebumen! 🚔🚦**
