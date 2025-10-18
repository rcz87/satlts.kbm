from flask import Flask, render_template, url_for
from markupsafe import Markup
import markdown
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')

def load_markdown(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        html = markdown.markdown(
            content, 
            extensions=['tables', 'fenced_code', 'nl2br']
        )
        
        return Markup(html)
    except FileNotFoundError:
        return Markup(f'<p>File {filename} tidak ditemukan.</p>')
    except Exception as e:
        return Markup(f'<p>Error: {str(e)}</p>')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
