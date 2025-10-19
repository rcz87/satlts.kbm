import os
import psycopg2
from flask import jsonify
import logging

def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

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
        
        # Nama opsional, tapi jika ada harus valid
        if nama and len(nama) > 100:
            return jsonify({'success': False, 'message': 'Nama terlalu panjang (maks 100 karakter)'}), 400
        
        # Email opsional
        if email and len(email) > 100:
            return jsonify({'success': False, 'message': 'Email terlalu panjang (maks 100 karakter)'}), 400
        
        if len(pesan) > 1000:
            return jsonify({'success': False, 'message': 'Pesan terlalu panjang (maks 1000 karakter)'}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Cek apakah tabel feedback sudah ada, jika belum buat
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
        
        # Insert feedback
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


def feedback_daftar_route():
    """Route untuk melihat semua feedback (admin)"""
    from flask import render_template_string
    
    logger = logging.getLogger(__name__)
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Cek apakah tabel feedback ada
        cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'feedback'
            )
        """)
        table_exists = cur.fetchone()[0]
        
        if not table_exists:
            cur.close()
            conn.close()
            return render_template_string('''
                <h2>Belum ada feedback</h2>
                <p>Tabel feedback belum dibuat. Feedback pertama akan membuat tabel otomatis.</p>
                <a href="/">Kembali ke Beranda</a>
            ''')
        
        cur.execute('''
            SELECT id, created_at, nama, email, kategori, pesan, status
            FROM feedback
            ORDER BY created_at DESC
        ''')
        
        feedbacks = cur.fetchall()
        total_feedback = len(feedbacks)
        
        cur.close()
        conn.close()
        
        # Generate HTML
        html = f'''
        <!DOCTYPE html>
        <html lang="id">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Daftar Feedback - SAMSAT Kebumen</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 20px;
                    margin: 0;
                }}
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 15px;
                    padding: 30px;
                    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                }}
                h1 {{
                    color: #1e3c72;
                    border-bottom: 3px solid #667eea;
                    padding-bottom: 15px;
                }}
                .stats {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 15px;
                    border-radius: 10px;
                    margin: 20px 0;
                    text-align: center;
                    font-size: 1.2em;
                }}
                .feedback-item {{
                    border: 2px solid #e0e0e0;
                    border-radius: 10px;
                    padding: 20px;
                    margin: 15px 0;
                    background: #f9f9f9;
                    transition: all 0.3s;
                }}
                .feedback-item:hover {{
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                    border-color: #667eea;
                }}
                .feedback-header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 10px;
                    flex-wrap: wrap;
                }}
                .feedback-meta {{
                    font-size: 0.9em;
                    color: #666;
                }}
                .kategori-badge {{
                    display: inline-block;
                    padding: 5px 12px;
                    border-radius: 20px;
                    font-size: 0.85em;
                    font-weight: 600;
                    margin-top: 5px;
                }}
                .kategori-saran {{ background: #3b82f6; color: white; }}
                .kategori-bug {{ background: #ef4444; color: white; }}
                .kategori-tampilan {{ background: #8b5cf6; color: white; }}
                .kategori-konten {{ background: #10b981; color: white; }}
                .kategori-lainnya {{ background: #6b7280; color: white; }}
                .feedback-pesan {{
                    margin-top: 15px;
                    padding: 15px;
                    background: white;
                    border-left: 4px solid #667eea;
                    border-radius: 5px;
                    line-height: 1.6;
                }}
                .back-button {{
                    display: inline-block;
                    background: #667eea;
                    color: white;
                    padding: 12px 25px;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: 600;
                    transition: all 0.3s;
                }}
                .back-button:hover {{
                    background: #5568d3;
                    transform: translateY(-2px);
                }}
                .no-feedback {{
                    text-align: center;
                    padding: 40px;
                    color: #666;
                    font-size: 1.1em;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📬 Daftar Feedback & Saran Pengembangan</h1>
                <div class="stats">
                    📊 Total Feedback: <strong>{total_feedback}</strong>
                </div>
        '''
        
        if total_feedback == 0:
            html += '''
                <div class="no-feedback">
                    <h2>📭 Belum ada feedback</h2>
                    <p>Belum ada feedback yang masuk. Jadilah yang pertama memberikan saran!</p>
                </div>
            '''
        else:
            for fb in feedbacks:
                fb_id, created_at, nama, email, kategori, pesan, status = fb
                
                # Format tanggal
                tanggal = created_at.strftime('%d %B %Y, %H:%M WIB')
                
                # Kategori class
                kategori_class = 'kategori-lainnya'
                if 'Fitur' in kategori:
                    kategori_class = 'kategori-saran'
                elif 'Bug' in kategori:
                    kategori_class = 'kategori-bug'
                elif 'Tampilan' in kategori:
                    kategori_class = 'kategori-tampilan'
                elif 'Konten' in kategori:
                    kategori_class = 'kategori-konten'
                
                html += f'''
                <div class="feedback-item">
                    <div class="feedback-header">
                        <div>
                            <strong style="font-size: 1.1em;">👤 {nama}</strong>
                            {f'<br><small>📧 {email}</small>' if email else ''}
                        </div>
                        <div class="feedback-meta">
                            <div>🕐 {tanggal}</div>
                            <div><span class="kategori-badge {kategori_class}">{kategori}</span></div>
                        </div>
                    </div>
                    <div class="feedback-pesan">
                        {pesan}
                    </div>
                </div>
                '''
        
        html += '''
                <div style="margin-top: 30px; text-align: center;">
                    <a href="/" class="back-button">🏠 Kembali ke Beranda</a>
                </div>
            </div>
        </body>
        </html>
        '''
        
        return html
    
    except Exception as e:
        logger.error(f"Feedback daftar error: {str(e)}")
        return f"Error: {str(e)}", 500
