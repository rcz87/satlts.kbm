#!/bin/bash

# ================================================
# DEPLOY SCRIPT VIA SSH
# Portal Satlantas Polres Kebumen
# ================================================
#
# Script ini melakukan deploy aplikasi ke VPS via SSH
# dari komputer lokal (VS Code Terminal atau PowerShell)
#
# CARA PAKAI:
#   chmod +x deploy/deploy-ssh.sh
#   ./deploy/deploy-ssh.sh
#
# PRASYARAT:
# - SSH sudah terkonfigurasi (bisa login tanpa error)
# - VPS sudah di-setup sesuai DEPLOYMENT.md
# - rsync terinstall di komputer lokal
#

# ================================================
# KONFIGURASI - SESUAIKAN DENGAN VPS ANDA
# ================================================

# IP Address VPS Hostinger
VPS_IP="${VPS_IP:-31.97.107.243}"

# Username di VPS
VPS_USER="${VPS_USER:-satlantas}"

# Port SSH
VPS_PORT="${VPS_PORT:-22}"

# Path aplikasi di VPS
VPS_APP_DIR="/var/www/satlantas"

# Nama service systemd
SERVICE_NAME="satlantas"

# ================================================
# WARNA OUTPUT
# ================================================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ================================================
# FUNGSI
# ================================================

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[OK]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# ================================================
# VALIDASI
# ================================================

if [ "$VPS_IP" = "YOUR_VPS_IP" ]; then
    log_error "VPS_IP belum dikonfigurasi!"
    echo ""
    echo "Cara setting:"
    echo "  1. Edit file ini dan ganti YOUR_VPS_IP dengan IP VPS Anda"
    echo "  2. Atau jalankan dengan environment variable:"
    echo "     VPS_IP=123.456.789.0 VPS_USER=satlantas ./deploy/deploy-ssh.sh"
    echo ""
    exit 1
fi

# ================================================
# MULAI DEPLOY
# ================================================

echo ""
echo "========================================"
echo " DEPLOY PORTAL SATLANTAS KE VPS"
echo "========================================"
echo " VPS: ${VPS_USER}@${VPS_IP}:${VPS_PORT}"
echo " Path: ${VPS_APP_DIR}"
echo "========================================"
echo ""

# 1. Test koneksi SSH
log_info "Testing SSH connection..."
ssh -p "$VPS_PORT" -o ConnectTimeout=10 "${VPS_USER}@${VPS_IP}" "echo 'SSH OK'" 2>/dev/null
if [ $? -ne 0 ]; then
    log_error "Tidak bisa konek ke VPS via SSH!"
    log_error "Pastikan: IP, username, port, dan password/key sudah benar"
    exit 1
fi
log_success "SSH connection OK"

# 2. Backup database di VPS sebelum deploy
log_info "Backup database di VPS..."
ssh -p "$VPS_PORT" "${VPS_USER}@${VPS_IP}" "
    if [ -f /opt/scripts/backup-db.sh ]; then
        /opt/scripts/backup-db.sh
    else
        echo 'Backup script not found, skipping backup'
    fi
"
log_success "Backup selesai"

# 3. Sync source code ke VPS (exclude file yang tidak perlu)
log_info "Uploading source code ke VPS..."
rsync -avz --progress \
    --exclude '.git' \
    --exclude '.env' \
    --exclude 'venv/' \
    --exclude '__pycache__/' \
    --exclude '*.pyc' \
    --exclude '.replit' \
    --exclude 'replit.nix' \
    --exclude '.upm/' \
    --exclude 'node_modules/' \
    --exclude '.cache/' \
    --exclude '*.log' \
    -e "ssh -p ${VPS_PORT}" \
    ./ "${VPS_USER}@${VPS_IP}:${VPS_APP_DIR}/"

if [ $? -ne 0 ]; then
    log_error "Upload gagal!"
    exit 1
fi
log_success "Upload source code selesai"

# 4. Install dependencies & restart service di VPS
log_info "Installing dependencies dan restart service..."
ssh -p "$VPS_PORT" "${VPS_USER}@${VPS_IP}" "
    cd ${VPS_APP_DIR}

    # Activate virtual environment
    source venv/bin/activate

    # Install/update dependencies
    pip install -r requirements.txt --quiet

    # Fix permissions
    sudo chown -R ${VPS_USER}:www-data ${VPS_APP_DIR}
    sudo chmod 755 ${VPS_APP_DIR}

    # Restart service
    sudo systemctl restart ${SERVICE_NAME}

    # Check status
    sleep 2
    sudo systemctl is-active ${SERVICE_NAME}
"

if [ $? -ne 0 ]; then
    log_warning "Service mungkin gagal restart. Cek log di VPS:"
    echo "  ssh ${VPS_USER}@${VPS_IP} 'sudo journalctl -u ${SERVICE_NAME} -n 50'"
    exit 1
fi
log_success "Deploy berhasil!"

# 5. Verifikasi
echo ""
echo "========================================"
log_success "DEPLOY SELESAI!"
echo "========================================"
echo ""
echo "Cek aplikasi di browser:"
echo "  http://${VPS_IP}"
echo ""
echo "Cek log di VPS:"
echo "  ssh ${VPS_USER}@${VPS_IP} 'sudo journalctl -u ${SERVICE_NAME} -f'"
echo ""
