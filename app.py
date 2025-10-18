from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
