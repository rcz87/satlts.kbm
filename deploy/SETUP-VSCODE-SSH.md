# Setup VS Code SSH ke VPS Hostinger

Panduan lengkap menghubungkan VS Code ke VPS untuk development & deployment Portal Satlantas.

---

## 1. Install Extension Remote-SSH

1. Buka VS Code
2. Tekan `Ctrl+Shift+X` (Extensions)
3. Cari **"Remote - SSH"** dari Microsoft
4. Klik **Install**

---

## 2. Konfigurasi SSH Config

### Langkah-langkah:

1. Tekan `Ctrl+Shift+P` di VS Code
2. Ketik: **Remote-SSH: Open SSH Configuration File**
3. Pilih file `~/.ssh/config` (atau `C:\Users\NamaAnda\.ssh\config` di Windows)
4. Tambahkan konfigurasi berikut:

```
Host satlantas-vps
    HostName IP_VPS_ANDA
    User root
    Port 22
    ServerAliveInterval 60
    ServerAliveCountMax 3
    Compression yes
```

5. Ganti `IP_VPS_ANDA` dengan IP VPS dari hPanel Hostinger
6. Save file (`Ctrl+S`)

> Template lengkap tersedia di: `deploy/ssh-config-example`

---

## 3. Connect ke VPS dari VS Code

1. Tekan `Ctrl+Shift+P`
2. Ketik: **Remote-SSH: Connect to Host**
3. Pilih **satlantas-vps**
4. Masukkan password VPS saat diminta
5. Tunggu VS Code setup server di VPS (pertama kali agak lama)
6. Setelah connected, klik **Open Folder** dan pilih `/var/www/satlantas`

---

## 4. Setup SSH Key (Opsional, Disarankan)

Agar tidak perlu ketik password setiap kali connect:

### Di komputer lokal (Terminal/PowerShell):

```bash
# Generate SSH Key
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_satlantas

# Copy key ke VPS
ssh-copy-id -i ~/.ssh/id_rsa_satlantas root@IP_VPS_ANDA
```

### Di Windows (PowerShell):

```powershell
# Generate SSH Key
ssh-keygen -t rsa -b 4096 -f $env:USERPROFILE\.ssh\id_rsa_satlantas

# Copy key ke VPS (manual)
type $env:USERPROFILE\.ssh\id_rsa_satlantas.pub | ssh root@IP_VPS_ANDA "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Update SSH Config:

```
Host satlantas-vps
    HostName IP_VPS_ANDA
    User satlantas
    Port 22
    IdentityFile ~/.ssh/id_rsa_satlantas
    ServerAliveInterval 60
    ServerAliveCountMax 3
    Compression yes
```

---

## 5. Deploy dari VS Code Terminal

Setelah connected ke VPS via SSH, buka Terminal di VS Code (`Ctrl+``) dan jalankan:

### Pertama kali (setup):
```bash
# Clone repository
cd /var/www
sudo git clone https://github.com/YOUR_USERNAME/portal-satlantas.git satlantas
cd satlantas

# Setup virtual environment
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
nano .env  # Edit dan isi nilai yang benar
```

### Update aplikasi:
```bash
cd /var/www/satlantas
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart satlantas
```

---

## 6. Deploy Otomatis (dari komputer lokal)

Gunakan script deploy yang sudah disediakan:

```bash
# Set IP VPS dan jalankan deploy
VPS_IP=123.456.789.0 VPS_USER=satlantas ./deploy/deploy-ssh.sh
```

Script ini akan:
- Test koneksi SSH
- Backup database di VPS
- Upload source code via rsync
- Install dependencies
- Restart service otomatis

---

## 7. Tips VS Code + SSH

### Extensions yang berguna di Remote:
- **Python** - syntax highlighting & linting
- **Pylance** - Python language server
- **GitLens** - Git integration
- **Thunder Client** - API testing

### Shortcut berguna:
- `Ctrl+Shift+P` - Command Palette
- `` Ctrl+` `` - Toggle Terminal
- `Ctrl+Shift+E` - File Explorer
- `Ctrl+Shift+G` - Git panel

### Monitor aplikasi dari VS Code Terminal:
```bash
# Cek status service
sudo systemctl status satlantas

# Lihat log real-time
sudo journalctl -u satlantas -f

# Cek Nginx
sudo systemctl status nginx
```

---

## Troubleshooting

### VS Code tidak bisa connect
```
# Cek koneksi dari terminal biasa dulu:
ssh root@IP_VPS_ANDA

# Jika timeout, cek firewall:
# Di VPS: sudo ufw allow OpenSSH
```

### Permission denied
```
# Pastikan user sudah benar di SSH config
# Cek password di hPanel Hostinger
# Atau pastikan SSH key sudah di-copy
```

### Connection keeps dropping
```
# Tambahkan di SSH config:
ServerAliveInterval 60
ServerAliveCountMax 3
```
