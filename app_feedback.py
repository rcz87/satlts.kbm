from flask import jsonify
import logging
import psycopg2

from db import get_db_connection


def feedback_submit_route():
    from flask import request

    logger = logging.getLogger(__name__)

    try:
        data = request.json

        if not data:
            logger.warning("Feedback submit: Empty request data")
            return jsonify({'success': False, 'message': 'Data tidak valid'}), 400

        nama = data.get('nama', '').strip()
        email = data.get('email', '').strip()
        kategori = data.get('kategori', '').strip()
        pesan = data.get('pesan', '').strip()

        # Validasi kategori
        ALLOWED_KATEGORI = [
            'Saran Fitur Baru',
            'Perbaikan Bug/Error',
            'Peningkatan Tampilan',
            'Konten & Informasi',
            'Lainnya'
        ]

        if not kategori or kategori not in ALLOWED_KATEGORI:
            logger.warning(f"Feedback submit: Invalid kategori '{kategori}'")
            return jsonify({'success': False, 'message': 'Kategori tidak valid'}), 400

        if not pesan or len(pesan) < 10:
            logger.info("Feedback submit: Pesan terlalu pendek")
            return jsonify({'success': False, 'message': 'Pesan minimal 10 karakter'}), 400

        if nama and len(nama) > 100:
            return jsonify({'success': False, 'message': 'Nama terlalu panjang (maks 100 karakter)'}), 400

        if email and len(email) > 100:
            return jsonify({'success': False, 'message': 'Email terlalu panjang (maks 100 karakter)'}), 400

        if len(pesan) > 1000:
            return jsonify({'success': False, 'message': 'Pesan terlalu panjang (maks 1000 karakter)'}), 400

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('''
            INSERT INTO feedback (nama, email, kategori, pesan)
            VALUES (%s, %s, %s, %s)
        ''', (nama if nama else 'Anonim', email if email else None, kategori, pesan))

        conn.commit()
        cur.close()
        conn.close()

        logger.info(f"Feedback submit success: kategori={kategori}, pesan_length={len(pesan)}")
        return jsonify({'success': True, 'message': 'Terima kasih! Feedback Anda telah berhasil dikirim.'})

    except ValueError as e:
        logger.error(f"Feedback submit ValueError: {str(e)}")
        return jsonify({'success': False, 'message': 'Data tidak valid'}), 400
    except psycopg2.Error as e:
        logger.error(f"Feedback submit DB error: {str(e)}")
        return jsonify({'success': False, 'message': 'Terjadi kesalahan database. Silakan coba lagi.'}), 500
    except Exception as e:
        logger.error(f"Feedback submit error: {str(e)}")
        return jsonify({'success': False, 'message': 'Terjadi kesalahan. Silakan coba lagi.'}), 500
