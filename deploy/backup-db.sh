#!/bin/bash

# ================================================
# DATABASE BACKUP SCRIPT
# Portal Satlantas Polres Kebumen
# ================================================
#
# Script ini melakukan backup database PostgreSQL secara otomatis
# dengan rotasi file backup (hanya simpan 7 backup terakhir)
#
# INSTRUKSI SETUP:
# 1. Copy script ke home directory atau /opt/scripts:
#    sudo cp deploy/backup-db.sh /opt/scripts/
#
# 2. Buat script executable:
#    sudo chmod +x /opt/scripts/backup-db.sh
#
# 3. Buat folder backup:
#    sudo mkdir -p /var/backups/satlantas
#    sudo chown satlantas:satlantas /var/backups/satlantas
#
# 4. Test manual:
#    /opt/scripts/backup-db.sh
#
# 5. Setup cron untuk backup otomatis setiap hari jam 2 pagi:
#    crontab -e
#    Tambahkan line:
#    0 2 * * * /opt/scripts/backup-db.sh >> /var/log/satlantas/backup.log 2>&1
#

# ================================================
# KONFIGURASI
# ================================================

# Lokasi backup
BACKUP_DIR="/var/backups/satlantas"

# Database credentials (ambil dari environment atau sesuaikan)
DB_NAME="${PGDATABASE:-satlantas_db}"
DB_USER="${PGUSER:-satlantas}"
DB_HOST="${PGHOST:-localhost}"
DB_PORT="${PGPORT:-5432}"

# Jumlah backup yang disimpan (older backups akan dihapus)
RETENTION_DAYS=7

# Timestamp untuk nama file
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/satlantas_db_${TIMESTAMP}.sql.gz"

# ================================================
# FUNGSI
# ================================================

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# ================================================
# BACKUP PROCESS
# ================================================

log_message "Starting database backup..."

# Cek apakah folder backup ada
if [ ! -d "$BACKUP_DIR" ]; then
    log_message "Creating backup directory: $BACKUP_DIR"
    mkdir -p "$BACKUP_DIR"
fi

# Lakukan backup dengan pg_dump dan compress dengan gzip
log_message "Backing up database: $DB_NAME"

PGPASSWORD="$PGPASSWORD" pg_dump \
    -h "$DB_HOST" \
    -p "$DB_PORT" \
    -U "$DB_USER" \
    -d "$DB_NAME" \
    --clean \
    --if-exists \
    --no-owner \
    --no-acl \
    | gzip > "$BACKUP_FILE"

# Cek apakah backup berhasil
if [ $? -eq 0 ]; then
    log_message "Backup completed successfully: $BACKUP_FILE"
    
    # Tampilkan ukuran file backup
    BACKUP_SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    log_message "Backup size: $BACKUP_SIZE"
else
    log_message "ERROR: Backup failed!"
    exit 1
fi

# ================================================
# CLEANUP OLD BACKUPS
# ================================================

log_message "Cleaning up old backups (keeping last $RETENTION_DAYS days)..."

# Hapus backup yang lebih lama dari RETENTION_DAYS
find "$BACKUP_DIR" -name "satlantas_db_*.sql.gz" -type f -mtime +$RETENTION_DAYS -delete

# Hitung jumlah backup yang tersisa
BACKUP_COUNT=$(find "$BACKUP_DIR" -name "satlantas_db_*.sql.gz" -type f | wc -l)
log_message "Total backups remaining: $BACKUP_COUNT"

log_message "Backup process completed!"

# ================================================
# RESTORE INSTRUCTIONS
# ================================================
# Untuk restore database dari backup:
#
# 1. Extract backup file:
#    gunzip -c /var/backups/satlantas/satlantas_db_TIMESTAMP.sql.gz > restore.sql
#
# 2. Restore ke database:
#    psql -h localhost -U satlantas -d satlantas_db -f restore.sql
#
# Atau dalam satu command:
#    gunzip -c /var/backups/satlantas/satlantas_db_TIMESTAMP.sql.gz | psql -h localhost -U satlantas -d satlantas_db
#
# CATATAN: Restore akan menimpa data yang ada, pastikan backup terlebih dahulu!
# ================================================
