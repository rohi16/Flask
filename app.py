from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download():
    directory = os.path.join(app.root_path, 'products')
    filename = 'Flask-Store.pdf'  # Make sure the file is named exactly this
    return send_from_directory(directory=directory, path=filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
