from flask import Flask, render_template, url_for, request, jsonify
from markupsafe import Markup
import markdown
import os
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Security: Require a proper secret key — no unsafe fallback
secret_key = os.environ.get('SESSION_SECRET')
if not secret_key:
    if app.debug:
        secret_key = 'dev-secret-key-only-for-local-debug'
    else:
        raise RuntimeError('SESSION_SECRET environment variable must be set in production')
app.secret_key = secret_key

# Security: Limit upload size to 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

from app_admin import admin_bp, limiter as admin_limiter
app.register_blueprint(admin_bp)
admin_limiter.init_app(app)

from db import init_tables
try:
    init_tables()
except Exception:
    app.logger.warning('Could not initialize database tables at startup')

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/satlantas.log', maxBytes=10240000, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Portal Satlantas startup')

# Security: CSRF Protection
csrf = CSRFProtect(app)

# Security: Rate Limiting (prevent DDoS/spam)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# Security: Secure session cookies
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
if not app.debug:
    app.config['SESSION_COOKIE_SECURE'] = True

def load_markdown(filename):
    try:
        filepath = os.path.join('content', filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        html = markdown.markdown(
            content,
            extensions=['tables', 'fenced_code', 'nl2br']
        )

        return Markup(html)
    except FileNotFoundError:
        app.logger.warning(f'Markdown file not found: {filename}')
        return Markup('<p>Konten tidak ditemukan.</p>')
    except Exception as e:
        app.logger.error(f'Error loading markdown {filename}: {str(e)}')
        return Markup('<p>Terjadi kesalahan saat memuat konten.</p>')

@app.route('/')
def index():
    content = load_markdown('content_home.md')
    return render_template('index.html', content=content, current_page='home')

@app.route('/5tahunan')
def tahunan():
    content = load_markdown('content_5tahunan.md')
    return render_template('index.html', content=content, current_page='5tahunan')

@app.route('/duplikat')
def duplikat():
    content = load_markdown('content_duplikat.md')
    return render_template('index.html', content=content, current_page='duplikat')

@app.route('/mutasi')
def mutasi():
    content = load_markdown('content_mutasi.md')
    return render_template('index.html', content=content, current_page='mutasi')

@app.route('/bbn')
def bbn():
    content = load_markdown('content_bbn.md')
    return render_template('index.html', content=content, current_page='bbn')

@app.route('/dasarhukum')
def dasarhukum():
    content = load_markdown('content_dasarhukum.md')
    return render_template('index.html', content=content, current_page='dasarhukum')

@app.route('/lihat-perpol')
def lihat_perpol():
    pdf_url = url_for('static', filename='documents/perpol-7-2021-regident.pdf')
    content = Markup(f'''
        <div class="pdf-container">
            <h2>📜 Peraturan Kepolisian No. 7 Tahun 2021</h2>
            <h3>Tentang Registrasi dan Identifikasi Kendaraan Bermotor</h3>
            <p>Peraturan ini menjadi dasar hukum pelaksanaan layanan SAMSAT di seluruh Indonesia.</p>
            <hr>
            <div class="pdf-viewer">
                <iframe src="{pdf_url}"
                        width="100%"
                        height="800px"
                        style="border: 1px solid #ddd; border-radius: 8px;">
                </iframe>
            </div>
            <p class="download-link">
                <a href="{pdf_url}"
                   download
                   style="display: inline-block; margin-top: 20px; padding: 12px 24px; background: #1e5aa8; color: white; text-decoration: none; border-radius: 5px;">
                   📥 Download PDF
                </a>
            </p>
        </div>
    ''')
    return render_template('index.html', content=content, current_page='dasarhukum')

@app.route('/lihat-uu-lalulintas')
def lihat_uu_lalulintas():
    pdf_url = url_for('static', filename='documents/uu-22-2009-lalulintas.pdf')
    content = Markup(f'''
        <div class="pdf-container">
            <h2>📜 UU No. 22 Tahun 2009</h2>
            <h3>Tentang Lalu Lintas dan Angkutan Jalan</h3>
            <p>Undang-undang yang mengatur tentang lalu lintas dan angkutan jalan di Indonesia.</p>
            <hr>
            <div class="pdf-viewer">
                <iframe src="{pdf_url}"
                        width="100%"
                        height="800px"
                        style="border: 1px solid #ddd; border-radius: 8px;">
                </iframe>
            </div>
            <p class="download-link">
                <a href="{pdf_url}"
                   download
                   style="display: inline-block; margin-top: 20px; padding: 12px 24px; background: #1e5aa8; color: white; text-decoration: none; border-radius: 5px;">
                   📥 Download PDF
                </a>
            </p>
        </div>
    ''')
    return render_template('index.html', content=content, current_page='dasarhukum')

@app.route('/galery')
def galery():
    content = load_markdown('content_galery.md')
    return render_template('index.html', content=content, current_page='galery')

@app.route('/ikm')
def ikm():
    content = load_markdown('content_ikm.md')
    return render_template('index.html', content=content, current_page='ikm')

# REGIDENT Routes
@app.route('/regident')
def regident():
    content = load_markdown('content_regident.md')
    return render_template('index.html', content=content, current_page='regident')

@app.route('/regident/stnk')
def regident_stnk():
    content = load_markdown('content_regident_stnk.md')
    return render_template('index.html', content=content, current_page='regident')

@app.route('/regident/sim')
def regident_sim():
    content = load_markdown('content_regident_sim.md')
    return render_template('index.html', content=content, current_page='regident')

@app.route('/regident/bpkb')
def regident_bpkb():
    content = load_markdown('content_regident_bpkb.md')
    return render_template('index.html', content=content, current_page='regident')

# GAKUM Routes
@app.route('/gakum')
def gakum():
    content = load_markdown('content_gakum.md')
    return render_template('index.html', content=content, current_page='gakum')

@app.route('/gakum/laka')
def gakum_laka():
    content = load_markdown('content_gakum_laka.md')
    return render_template('index.html', content=content, current_page='gakum')

@app.route('/gakum/tilang')
def gakum_tilang():
    content = load_markdown('content_gakum_tilang.md')
    return render_template('index.html', content=content, current_page='gakum')

# PATWAL Route
@app.route('/patwal')
def patwal():
    content = load_markdown('content_patwal.md')
    return render_template('index.html', content=content, current_page='patwal')

# KAMSEL Route
@app.route('/kamsel')
def kamsel():
    content = load_markdown('content_kamsel.md')
    return render_template('index.html', content=content, current_page='kamsel')

# URMIN Route
@app.route('/urmin')
def urmin():
    content = load_markdown('content_urmin.md')
    return render_template('index.html', content=content, current_page='urmin')

@app.route('/ikm/submit', methods=['POST'])
@limiter.limit("50 per day")
def ikm_submit():
    from app_ikm import ikm_submit_route
    return ikm_submit_route()

@app.route('/ikm/hasil')
def ikm_hasil():
    from app_ikm import ikm_hasil_route
    return ikm_hasil_route()

# Feedback routes
@app.route('/feedback/submit', methods=['POST'])
@limiter.limit("20 per hour")
def feedback_submit():
    from app_feedback import feedback_submit_route
    return feedback_submit_route()

# Security: Add security headers to all responses
@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data:; "
        "font-src 'self'; "
        "frame-ancestors 'self';"
    )
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    if not app.debug:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
