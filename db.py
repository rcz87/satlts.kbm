import os
import psycopg2


def get_db_connection():
    return psycopg2.connect(os.environ['DATABASE_URL'])


def init_tables():
    """Create tables if they don't exist. Call once at app startup."""
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS survei_ikm (
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                jenis_layanan VARCHAR(100),
                persyaratan INTEGER NOT NULL,
                prosedur INTEGER NOT NULL,
                waktu_pelayanan INTEGER NOT NULL,
                biaya_tarif INTEGER NOT NULL,
                produk_layanan INTEGER NOT NULL,
                kompetensi_petugas INTEGER NOT NULL,
                perilaku_petugas INTEGER NOT NULL,
                maklumat_pelayanan INTEGER NOT NULL,
                penanganan_pengaduan INTEGER NOT NULL,
                komentar TEXT,
                rata_rata NUMERIC(5,2)
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                nama VARCHAR(100),
                email VARCHAR(100),
                kategori VARCHAR(50) NOT NULL,
                pesan TEXT NOT NULL,
                status VARCHAR(20) DEFAULT 'baru'
            )
        """)
        conn.commit()
    finally:
        cur.close()
        conn.close()
