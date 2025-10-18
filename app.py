from flask import Flask, render_template
from markupsafe import Markup
import markdown
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')

@app.route('/')
def index():
    try:
        with open('samsat_infoboard.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        html = markdown.markdown(
            content, 
            extensions=['tables', 'fenced_code', 'nl2br']
        )
        
        return render_template('index.html', content=Markup(html))
    except FileNotFoundError:
        return render_template('index.html', content=Markup('<p>File samsat_infoboard.md tidak ditemukan.</p>'))
    except Exception as e:
        return render_template('index.html', content=Markup(f'<p>Error: {str(e)}</p>'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
