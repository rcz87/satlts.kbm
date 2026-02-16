from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from functools import wraps
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

from db import get_db_connection

logger = logging.getLogger(__name__)

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="memory://"
)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            flash('Silakan login terlebih dahulu.', 'warning')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/login', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            flash('Username dan password harus diisi.', 'danger')
            return render_template('admin/login.html')

        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        try:
            cur.execute(
                'SELECT * FROM admin_users WHERE username = %s AND is_active = TRUE',
                (username,)
            )
            user = cur.fetchone()

            if user and check_password_hash(user['password_hash'], password):
                session['admin_logged_in'] = True
                session['admin_username'] = user['username']
                session['admin_fullname'] = user['full_name']
                session['admin_id'] = user['id']

                cur.execute(
                    'UPDATE admin_users SET last_login = %s WHERE id = %s',
                    (datetime.now(), user['id'])
                )
                conn.commit()

                flash(f'Selamat datang, {user["full_name"]}!', 'success')
                return redirect(url_for('admin.dashboard'))
            else:
                flash('Username atau password salah.', 'danger')
        except Exception as e:
            logger.error(f'Admin login error: {str(e)}')
            flash('Terjadi kesalahan sistem. Silakan coba lagi.', 'danger')
        finally:
            cur.close()
            conn.close()

    if 'admin_logged_in' in session:
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/login.html')

@admin_bp.route('/logout')
def logout():
    session.clear()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('admin.login'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute('SELECT COUNT(*) as total FROM survei_ikm')
        ikm_result = cur.fetchone()
        ikm_count = ikm_result['total'] if ikm_result else 0

        cur.execute('SELECT COUNT(*) as total FROM feedback')
        feedback_result = cur.fetchone()
        feedback_count = feedback_result['total'] if feedback_result else 0

        cur.execute('SELECT COUNT(*) as total FROM kegiatan')
        kegiatan_result = cur.fetchone()
        kegiatan_count = kegiatan_result['total'] if kegiatan_result else 0

        cur.execute('''
            SELECT
                AVG(rata_rata) * 25 as avg_ikm
            FROM survei_ikm
        ''')
        avg_ikm_result = cur.fetchone()
        avg_ikm = round(avg_ikm_result['avg_ikm'], 2) if avg_ikm_result and avg_ikm_result['avg_ikm'] else 0

        cur.execute('''
            SELECT DATE(created_at) as tanggal, COUNT(*) as jumlah
            FROM survei_ikm
            WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
            GROUP BY DATE(created_at)
            ORDER BY tanggal DESC
            LIMIT 7
        ''')
        ikm_weekly = cur.fetchall()

        cur.execute('''
            SELECT created_at, jenis_layanan, komentar
            FROM survei_ikm
            WHERE komentar IS NOT NULL AND komentar != ''
            ORDER BY created_at DESC
            LIMIT 5
        ''')
        recent_comments = cur.fetchall()

        cur.execute('''
            SELECT created_at, nama, pesan
            FROM feedback
            ORDER BY created_at DESC
            LIMIT 5
        ''')
        recent_feedback = cur.fetchall()

        stats = {
            'ikm_count': ikm_count,
            'feedback_count': feedback_count,
            'kegiatan_count': kegiatan_count,
            'avg_ikm': avg_ikm,
            'ikm_weekly': ikm_weekly,
            'recent_comments': recent_comments,
            'recent_feedback': recent_feedback
        }

        return render_template('admin/dashboard.html', stats=stats)

    except Exception as e:
        logger.error(f'Dashboard error: {str(e)}')
        flash('Terjadi kesalahan saat mengambil data.', 'danger')
        return render_template('admin/dashboard.html', stats={})
    finally:
        cur.close()
        conn.close()

@admin_bp.route('/ikm')
@login_required
def ikm_list():
    page = request.args.get('page', 1, type=int)
    per_page = 20

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute('SELECT COUNT(*) as total FROM survei_ikm')
        total_result = cur.fetchone()
        total = total_result['total'] if total_result else 0

        offset = (page - 1) * per_page
        cur.execute('''
            SELECT
                id, jenis_layanan, created_at,
                rata_rata * 25 as score
            FROM survei_ikm
            ORDER BY created_at DESC
            LIMIT %s OFFSET %s
        ''', (per_page, offset))
        responses = cur.fetchall()

        total_pages = (total + per_page - 1) // per_page

        return render_template('admin/ikm_list.html',
                             responses=responses,
                             page=page,
                             total_pages=total_pages,
                             total=total)

    except Exception as e:
        logger.error(f'IKM list error: {str(e)}')
        flash('Terjadi kesalahan saat mengambil data.', 'danger')
        return render_template('admin/ikm_list.html', responses=[], page=1, total_pages=0, total=0)
    finally:
        cur.close()
        conn.close()

@admin_bp.route('/ikm/<int:id>')
@login_required
def ikm_detail(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute('SELECT * FROM survei_ikm WHERE id = %s', (id,))
        response = cur.fetchone()

        if not response:
            flash('Data tidak ditemukan.', 'warning')
            return redirect(url_for('admin.ikm_list'))

        return render_template('admin/ikm_detail.html', response=response)

    except Exception as e:
        logger.error(f'IKM detail error: {str(e)}')
        flash('Terjadi kesalahan saat mengambil data.', 'danger')
        return redirect(url_for('admin.ikm_list'))
    finally:
        cur.close()
        conn.close()

@admin_bp.route('/feedback')
@login_required
def feedback_list():
    page = request.args.get('page', 1, type=int)
    per_page = 20

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute('SELECT COUNT(*) as total FROM feedback')
        total_result = cur.fetchone()
        total = total_result['total'] if total_result else 0

        offset = (page - 1) * per_page
        cur.execute('''
            SELECT *
            FROM feedback
            ORDER BY created_at DESC
            LIMIT %s OFFSET %s
        ''', (per_page, offset))
        feedbacks = cur.fetchall()

        total_pages = (total + per_page - 1) // per_page

        return render_template('admin/feedback_list.html',
                             feedbacks=feedbacks,
                             page=page,
                             total_pages=total_pages,
                             total=total)

    except Exception as e:
        logger.error(f'Feedback list error: {str(e)}')
        flash('Terjadi kesalahan saat mengambil data.', 'danger')
        return render_template('admin/feedback_list.html', feedbacks=[], page=1, total_pages=0, total=0)
    finally:
        cur.close()
        conn.close()

@admin_bp.route('/feedback/delete/<int:id>', methods=['POST'])
@login_required
def feedback_delete(id):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute('DELETE FROM feedback WHERE id = %s', (id,))
        conn.commit()
        flash('Feedback berhasil dihapus.', 'success')
    except Exception as e:
        logger.error(f'Feedback delete error: {str(e)}')
        flash('Terjadi kesalahan saat menghapus data.', 'danger')
    finally:
        cur.close()
        conn.close()

    return redirect(url_for('admin.feedback_list'))

@admin_bp.route('/gallery')
@login_required
def gallery_manage():
    import glob

    gallery_path = 'static/images/galery'
    images = []

    if os.path.exists(gallery_path):
        image_files = glob.glob(f'{gallery_path}/*.jpg') + glob.glob(f'{gallery_path}/*.jpeg') + glob.glob(f'{gallery_path}/*.png')
        images = [os.path.basename(f) for f in image_files]
        images.sort()

    return render_template('admin/gallery.html', images=images)

@admin_bp.route('/gallery/upload', methods=['POST'])
@login_required
def gallery_upload():
    if 'photo' not in request.files:
        flash('Tidak ada file yang dipilih.', 'warning')
        return redirect(url_for('admin.gallery_manage'))

    file = request.files['photo']

    if not file.filename:
        flash('Tidak ada file yang dipilih.', 'warning')
        return redirect(url_for('admin.gallery_manage'))

    if file and file.filename and allowed_file(file.filename):
        from werkzeug.utils import secure_filename
        import time

        filename = secure_filename(file.filename)
        timestamp = str(int(time.time()))
        new_filename = f"foto-{timestamp}-{filename}"

        gallery_path = 'static/images/galery'
        os.makedirs(gallery_path, exist_ok=True)

        file.save(os.path.join(gallery_path, new_filename))
        flash(f'Foto {new_filename} berhasil diupload.', 'success')
    else:
        flash('Format file tidak didukung. Gunakan JPG, JPEG, atau PNG.', 'danger')

    return redirect(url_for('admin.gallery_manage'))

@admin_bp.route('/gallery/delete/<filename>', methods=['POST'])
@login_required
def gallery_delete(filename):
    from werkzeug.utils import secure_filename

    filename = secure_filename(filename)
    filepath = os.path.join('static/images/galery', filename)

    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            flash(f'Foto {filename} berhasil dihapus.', 'success')
        else:
            flash('File tidak ditemukan.', 'warning')
    except Exception as e:
        logger.error(f'Gallery delete error: {str(e)}')
        flash('Terjadi kesalahan saat menghapus file.', 'danger')

    return redirect(url_for('admin.gallery_manage'))

@admin_bp.route('/documents')
@login_required
def documents_manage():
    import glob

    docs_path = 'static/documents'
    documents = []

    if os.path.exists(docs_path):
        doc_files = glob.glob(f'{docs_path}/*.pdf')
        documents = [os.path.basename(f) for f in doc_files]
        documents.sort()

    return render_template('admin/documents.html', documents=documents)

@admin_bp.route('/documents/upload', methods=['POST'])
@login_required
def documents_upload():
    if 'document' not in request.files:
        flash('Tidak ada file yang dipilih.', 'warning')
        return redirect(url_for('admin.documents_manage'))

    file = request.files['document']

    if not file.filename:
        flash('Tidak ada file yang dipilih.', 'warning')
        return redirect(url_for('admin.documents_manage'))

    if file and file.filename and file.filename.lower().endswith('.pdf'):
        from werkzeug.utils import secure_filename

        filename = secure_filename(file.filename)

        docs_path = 'static/documents'
        os.makedirs(docs_path, exist_ok=True)

        file.save(os.path.join(docs_path, filename))
        flash(f'Dokumen {filename} berhasil diupload.', 'success')
    else:
        flash('Format file tidak didukung. Gunakan PDF.', 'danger')

    return redirect(url_for('admin.documents_manage'))

@admin_bp.route('/documents/delete/<filename>', methods=['POST'])
@login_required
def documents_delete(filename):
    from werkzeug.utils import secure_filename

    filename = secure_filename(filename)
    filepath = os.path.join('static/documents', filename)

    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            flash(f'Dokumen {filename} berhasil dihapus.', 'success')
        else:
            flash('File tidak ditemukan.', 'warning')
    except Exception as e:
        logger.error(f'Document delete error: {str(e)}')
        flash('Terjadi kesalahan saat menghapus file.', 'danger')

    return redirect(url_for('admin.documents_manage'))

UNIT_CHOICES = ['REGIDENT', 'GAKUM', 'PATWAL', 'KAMSEL', 'URMIN']

# ==================== KEGIATAN CRUD ====================

@admin_bp.route('/kegiatan')
@login_required
def kegiatan_list():
    page = request.args.get('page', 1, type=int)
    unit_filter = request.args.get('unit', '')
    per_page = 20

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        if unit_filter and unit_filter in UNIT_CHOICES:
            cur.execute('SELECT COUNT(*) as total FROM kegiatan WHERE unit = %s', (unit_filter,))
        else:
            cur.execute('SELECT COUNT(*) as total FROM kegiatan')
            unit_filter = ''

        total_result = cur.fetchone()
        total = total_result['total'] if total_result else 0

        offset = (page - 1) * per_page
        if unit_filter:
            cur.execute('''
                SELECT * FROM kegiatan
                WHERE unit = %s
                ORDER BY tanggal_kegiatan DESC, created_at DESC
                LIMIT %s OFFSET %s
            ''', (unit_filter, per_page, offset))
        else:
            cur.execute('''
                SELECT * FROM kegiatan
                ORDER BY tanggal_kegiatan DESC, created_at DESC
                LIMIT %s OFFSET %s
            ''', (per_page, offset))

        kegiatan_items = cur.fetchall()
        total_pages = (total + per_page - 1) // per_page

        return render_template('admin/kegiatan_list.html',
                             kegiatan_items=kegiatan_items,
                             page=page,
                             total_pages=total_pages,
                             total=total,
                             unit_filter=unit_filter,
                             unit_choices=UNIT_CHOICES)

    except Exception as e:
        logger.error(f'Kegiatan list error: {str(e)}')
        flash('Terjadi kesalahan saat mengambil data.', 'danger')
        return render_template('admin/kegiatan_list.html',
                             kegiatan_items=[], page=1, total_pages=0, total=0,
                             unit_filter='', unit_choices=UNIT_CHOICES)
    finally:
        cur.close()
        conn.close()

@admin_bp.route('/kegiatan/tambah', methods=['GET', 'POST'])
@login_required
def kegiatan_tambah():
    if request.method == 'POST':
        judul = request.form.get('judul', '').strip()
        isi = request.form.get('isi', '').strip()
        unit = request.form.get('unit', '').strip()
        tanggal = request.form.get('tanggal_kegiatan', '').strip()

        if not judul or not isi or not unit or not tanggal:
            flash('Semua field wajib diisi.', 'danger')
            return render_template('admin/kegiatan_form.html',
                                 mode='tambah', unit_choices=UNIT_CHOICES,
                                 kegiatan={'judul': judul, 'isi': isi, 'unit': unit, 'tanggal_kegiatan': tanggal})

        if unit not in UNIT_CHOICES:
            flash('Unit tidak valid.', 'danger')
            return render_template('admin/kegiatan_form.html',
                                 mode='tambah', unit_choices=UNIT_CHOICES,
                                 kegiatan={'judul': judul, 'isi': isi, 'unit': unit, 'tanggal_kegiatan': tanggal})

        foto_filename = None
        if 'foto' in request.files:
            file = request.files['foto']
            if file and file.filename and allowed_file(file.filename):
                from werkzeug.utils import secure_filename
                import time
                filename = secure_filename(file.filename)
                timestamp = str(int(time.time()))
                foto_filename = f"kegiatan-{timestamp}-{filename}"

                upload_path = 'static/images/kegiatan'
                os.makedirs(upload_path, exist_ok=True)
                file.save(os.path.join(upload_path, foto_filename))

        conn = get_db_connection()
        cur = conn.cursor()

        try:
            cur.execute('''
                INSERT INTO kegiatan (judul, isi, foto, unit, tanggal_kegiatan)
                VALUES (%s, %s, %s, %s, %s)
            ''', (judul, isi, foto_filename, unit, tanggal))
            conn.commit()
            flash('Kegiatan berhasil ditambahkan.', 'success')
            return redirect(url_for('admin.kegiatan_list'))
        except Exception as e:
            logger.error(f'Kegiatan tambah error: {str(e)}')
            flash('Terjadi kesalahan saat menyimpan data.', 'danger')
        finally:
            cur.close()
            conn.close()

    return render_template('admin/kegiatan_form.html',
                         mode='tambah', unit_choices=UNIT_CHOICES, kegiatan={})

@admin_bp.route('/kegiatan/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def kegiatan_edit(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        if request.method == 'POST':
            judul = request.form.get('judul', '').strip()
            isi = request.form.get('isi', '').strip()
            unit = request.form.get('unit', '').strip()
            tanggal = request.form.get('tanggal_kegiatan', '').strip()

            if not judul or not isi or not unit or not tanggal:
                flash('Semua field wajib diisi.', 'danger')
                cur.execute('SELECT * FROM kegiatan WHERE id = %s', (id,))
                kegiatan = cur.fetchone()
                return render_template('admin/kegiatan_form.html',
                                     mode='edit', unit_choices=UNIT_CHOICES, kegiatan=kegiatan)

            if unit not in UNIT_CHOICES:
                flash('Unit tidak valid.', 'danger')
                cur.execute('SELECT * FROM kegiatan WHERE id = %s', (id,))
                kegiatan = cur.fetchone()
                return render_template('admin/kegiatan_form.html',
                                     mode='edit', unit_choices=UNIT_CHOICES, kegiatan=kegiatan)

            foto_filename = None
            if 'foto' in request.files:
                file = request.files['foto']
                if file and file.filename and allowed_file(file.filename):
                    from werkzeug.utils import secure_filename
                    import time
                    filename = secure_filename(file.filename)
                    timestamp = str(int(time.time()))
                    foto_filename = f"kegiatan-{timestamp}-{filename}"

                    upload_path = 'static/images/kegiatan'
                    os.makedirs(upload_path, exist_ok=True)
                    file.save(os.path.join(upload_path, foto_filename))

            if foto_filename:
                cur.execute('''
                    UPDATE kegiatan
                    SET judul = %s, isi = %s, foto = %s, unit = %s, tanggal_kegiatan = %s,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                ''', (judul, isi, foto_filename, unit, tanggal, id))
            else:
                cur.execute('''
                    UPDATE kegiatan
                    SET judul = %s, isi = %s, unit = %s, tanggal_kegiatan = %s,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                ''', (judul, isi, unit, tanggal, id))

            conn.commit()
            flash('Kegiatan berhasil diperbarui.', 'success')
            return redirect(url_for('admin.kegiatan_list'))

        cur.execute('SELECT * FROM kegiatan WHERE id = %s', (id,))
        kegiatan = cur.fetchone()

        if not kegiatan:
            flash('Kegiatan tidak ditemukan.', 'warning')
            return redirect(url_for('admin.kegiatan_list'))

        return render_template('admin/kegiatan_form.html',
                             mode='edit', unit_choices=UNIT_CHOICES, kegiatan=kegiatan)

    except Exception as e:
        logger.error(f'Kegiatan edit error: {str(e)}')
        flash('Terjadi kesalahan.', 'danger')
        return redirect(url_for('admin.kegiatan_list'))
    finally:
        cur.close()
        conn.close()

@admin_bp.route('/kegiatan/hapus/<int:id>', methods=['POST'])
@login_required
def kegiatan_hapus(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute('SELECT foto FROM kegiatan WHERE id = %s', (id,))
        kegiatan = cur.fetchone()
        if kegiatan and kegiatan['foto']:
            filepath = os.path.join('static/images/kegiatan', kegiatan['foto'])
            if os.path.exists(filepath):
                os.remove(filepath)

        cur.execute('DELETE FROM kegiatan WHERE id = %s', (id,))
        conn.commit()
        flash('Kegiatan berhasil dihapus.', 'success')
    except Exception as e:
        logger.error(f'Kegiatan hapus error: {str(e)}')
        flash('Terjadi kesalahan saat menghapus data.', 'danger')
    finally:
        cur.close()
        conn.close()

    return redirect(url_for('admin.kegiatan_list'))


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
