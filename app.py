from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '''
    <h2>Descargar video de Instagram</h2>
    <form method="POST" action="/download">
        <input type="text" name="url" placeholder="Pega el link de Instagram" required>
        <button type="submit">Descargar</button>
    </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
