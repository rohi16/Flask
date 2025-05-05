from flask import Flask, send_file

app = Flask(__name__)

# Route to show the "Coming Soon" message
@app.route('/')
def home():
    return '''
    <h2>Welcome to Our eBook Page!</h2>
    <p>The eBook is coming soon. Check back later!</p>
    '''

# Route for downloading the real eBook (update when you're ready)
@app.route('/download_ebook')
def download_ebook():
    # For now, it's a placeholder message.
    return "The eBook will be available soon. Stay tuned!"

# Uncomment below code when you're ready to serve the real eBook
# @app.route('/download_ebook')
# def download_ebook():
#     return send_file('static/real_ebook.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
