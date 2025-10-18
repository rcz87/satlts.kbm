# File terpisah untuk routes IKM
from flask import jsonify, render_template
from markupsafe import Markup
import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

def ikm_submit_route():
    from flask import request
    import logging
    
    logger = logging.getLogger(__name__)
    
    try:
        data = request.json
        
        if not data:
            logger.warning("IKM submit: Empty request data")
            return jsonify({'success': False, 'message': 'Data tidak valid'}), 400
        
        persyaratan = int(data.get('persyaratan', 0))
        prosedur = int(data.get('prosedur', 0))
        waktu_pelayanan = int(data.get('waktu_pelayanan', 0))
        biaya_tarif = int(data.get('biaya_tarif', 0))
        produk_layanan = int(data.get('produk_layanan', 0))
        kompetensi_petugas = int(data.get('kompetensi_petugas', 0))
        perilaku_petugas = int(data.get('perilaku_petugas', 0))
        maklumat_pelayanan = int(data.get('maklumat_pelayanan', 0))
        penanganan_pengaduan = int(data.get('penanganan_pengaduan', 0))
        komentar = data.get('komentar', '')
        jenis_layanan = data.get('jenis_layanan', '').strip()
        
        # Security: Whitelist validation for jenis_layanan
        ALLOWED_JENIS_LAYANAN = [
            'Pembayaran Pajak Tahunan',
            'Pembayaran Pajak 5 Tahunan',
            'Duplikat STNK',
            'Mutasi Masuk',
            'Mutasi Keluar',
            'BBN 1 (Kendaraan Baru)',
            'BBN 2 (Balik Nama)',
            'Lainnya'
        ]
        
        if not jenis_layanan:
            logger.info("IKM submit: Missing jenis_layanan")
            return jsonify({'success': False, 'message': 'Mohon pilih jenis layanan'}), 400
        
        if jenis_layanan not in ALLOWED_JENIS_LAYANAN:
            logger.warning(f"IKM submit: Invalid jenis_layanan '{jenis_layanan}'")
            return jsonify({'success': False, 'message': 'Jenis layanan tidak valid'}), 400
        
        if any(r < 1 or r > 4 for r in [persyaratan, prosedur, waktu_pelayanan, biaya_tarif, 
                                         produk_layanan, kompetensi_petugas, perilaku_petugas, 
                                         maklumat_pelayanan, penanganan_pengaduan]):
            logger.info("IKM submit: Invalid rating values")
            return jsonify({'success': False, 'message': 'Mohon berikan penilaian untuk semua aspek (1-4 bintang)'}), 400
        
        rata_rata = (persyaratan + prosedur + waktu_pelayanan + biaya_tarif + produk_layanan + 
                     kompetensi_petugas + perilaku_petugas + maklumat_pelayanan + penanganan_pengaduan) / 9.0
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO survei_ikm 
            (persyaratan, prosedur, waktu_pelayanan, biaya_tarif, produk_layanan, 
             kompetensi_petugas, perilaku_petugas, maklumat_pelayanan, penanganan_pengaduan, 
             komentar, jenis_layanan, rata_rata)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (persyaratan, prosedur, waktu_pelayanan, biaya_tarif, produk_layanan,
              kompetensi_petugas, perilaku_petugas, maklumat_pelayanan, penanganan_pengaduan,
              komentar, jenis_layanan, rata_rata))
        conn.commit()
        cur.close()
        conn.close()
        
        logger.info(f"IKM submit success: jenis_layanan={jenis_layanan}, rata_rata={rata_rata:.2f}")
        return jsonify({'success': True, 'message': 'Terima kasih! Penilaian Anda telah berhasil disimpan.'})
    
    except ValueError as e:
        logger.error(f"IKM submit ValueError: {str(e)}")
        return jsonify({'success': False, 'message': 'Format data tidak valid'}), 400
    except psycopg2.Error as e:
        logger.error(f"IKM submit Database error: {str(e)}")
        return jsonify({'success': False, 'message': 'Terjadi kesalahan saat menyimpan data'}), 500
    except Exception as e:
        logger.error(f"IKM submit Unexpected error: {str(e)}", exc_info=True)
        return jsonify({'success': False, 'message': 'Terjadi kesalahan sistem'}), 500

def ikm_hasil_route():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute('''
            SELECT 
                COUNT(*) as total_responden,
                ROUND(AVG(persyaratan), 2) as avg_persyaratan,
                ROUND(AVG(prosedur), 2) as avg_prosedur,
                ROUND(AVG(waktu_pelayanan), 2) as avg_waktu_pelayanan,
                ROUND(AVG(biaya_tarif), 2) as avg_biaya_tarif,
                ROUND(AVG(produk_layanan), 2) as avg_produk_layanan,
                ROUND(AVG(kompetensi_petugas), 2) as avg_kompetensi_petugas,
                ROUND(AVG(perilaku_petugas), 2) as avg_perilaku_petugas,
                ROUND(AVG(maklumat_pelayanan), 2) as avg_maklumat_pelayanan,
                ROUND(AVG(penanganan_pengaduan), 2) as avg_penanganan_pengaduan,
                ROUND(AVG(rata_rata), 2) as ikm_total
            FROM survei_ikm
        ''')
        stats = cur.fetchone()
        
        cur.close()
        conn.close()
        
        if stats['total_responden'] == 0:
            stats = {
                'total_responden': 0,
                'ikm_total': 0,
                'avg_persyaratan': 0,
                'avg_prosedur': 0,
                'avg_waktu_pelayanan': 0,
                'avg_biaya_tarif': 0,
                'avg_produk_layanan': 0,
                'avg_kompetensi_petugas': 0,
                'avg_perilaku_petugas': 0,
                'avg_maklumat_pelayanan': 0,
                'avg_penanganan_pengaduan': 0
            }
        
        ikm_nilai = float(stats['ikm_total']) * 25 if stats['ikm_total'] else 0
        
        if ikm_nilai >= 88.31:
            kategori = "A - Sangat Baik"
            warna = "#10b981"
        elif ikm_nilai >= 76.61:
            kategori = "B - Baik"
            warna = "#3b82f6"
        elif ikm_nilai >= 65.00:
            kategori = "C - Kurang Baik"
            warna = "#f59e0b"
        else:
            kategori = "D - Tidak Baik"
            warna = "#ef4444"
        
        html_parts = []
        html_parts.append('<div class="ikm-hasil-container">')
        html_parts.append('<h1>Hasil Indeks Kepuasan Masyarakat</h1>')
        html_parts.append('<p class="ikm-subtitle">Data survei kepuasan pelayanan SAMSAT Kebumen</p>')
        
        html_parts.append('<div class="ikm-summary">')
        html_parts.append('<div class="ikm-card ikm-card-primary">')
        html_parts.append('<div class="ikm-card-icon">🎯</div>')
        html_parts.append('<div class="ikm-card-content">')
        html_parts.append('<div class="ikm-card-label">Nilai IKM</div>')
        html_parts.append(f'<div class="ikm-card-value" style="color: {warna};">{ikm_nilai:.2f}</div>')
        html_parts.append(f'<div class="ikm-card-category" style="color: {warna};">{kategori}</div>')
        html_parts.append('</div></div>')
        
        html_parts.append('<div class="ikm-card"><div class="ikm-card-icon">👥</div><div class="ikm-card-content">')
        html_parts.append('<div class="ikm-card-label">Total Responden</div>')
        html_parts.append(f'<div class="ikm-card-value">{stats["total_responden"]}</div>')
        html_parts.append('</div></div>')
        
        html_parts.append('<div class="ikm-card"><div class="ikm-card-icon">⭐</div><div class="ikm-card-content">')
        html_parts.append('<div class="ikm-card-label">Rata-rata</div>')
        html_parts.append(f'<div class="ikm-card-value">{stats["ikm_total"]:.2f} / 4</div>')
        html_parts.append('</div></div></div>')
        
        html_parts.append('<div class="ikm-section"><h2>Penilaian Per Aspek Pelayanan</h2><div class="ikm-aspects">')
        
        aspects = [
            ('1. Persyaratan', stats['avg_persyaratan']),
            ('2. Prosedur', stats['avg_prosedur']),
            ('3. Waktu Pelayanan', stats['avg_waktu_pelayanan']),
            ('4. Biaya/Tarif', stats['avg_biaya_tarif']),
            ('5. Produk Layanan', stats['avg_produk_layanan']),
            ('6. Kompetensi Petugas', stats['avg_kompetensi_petugas']),
            ('7. Perilaku Petugas', stats['avg_perilaku_petugas']),
            ('8. Sarana/Prasarana', stats['avg_maklumat_pelayanan']),
            ('9. Penanganan Pengaduan', stats['avg_penanganan_pengaduan'])
        ]
        
        for label, nilai in aspects:
            nilai_float = float(nilai) if nilai else 0
            width = (nilai_float / 4.0) * 100
            html_parts.append(f'<div class="ikm-aspect-item"><div class="ikm-aspect-label">{label}</div>')
            html_parts.append(f'<div class="ikm-aspect-rating"><div class="ikm-progress-bar">')
            html_parts.append(f'<div class="ikm-progress-fill" style="width: {width}%;"></div></div>')
            html_parts.append(f'<span class="ikm-aspect-value">{nilai_float:.2f} / 4</span></div></div>')
        
        html_parts.append('</div></div>')
        
        html_parts.append('<div class="ikm-back-button"><a href="/ikm" class="btn-back">Kembali ke Survei</a></div>')
        html_parts.append('</div>')
        
        content = Markup(''.join(html_parts))
        
        return render_template('index.html', content=content, current_page='ikm')
    
    except Exception as e:
        print(f"Error: {str(e)}")
        content = Markup(f'<div class="error-message"><h2>Terjadi Kesalahan</h2><p>{str(e)}</p><a href="/ikm">Kembali ke Survei</a></div>')
        return render_template('index.html', content=content, current_page='ikm')
