from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='.')


# Serve HTML pages (with and without .html extensions)
@app.route('/')
@app.route('/index.html')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/about')
@app.route('/about.html')
def about():
    return send_from_directory('.', 'about.html')

@app.route('/projects')
@app.route('/projects.html')
def projects():
    return send_from_directory('.', 'projects.html')

@app.route('/resume')
@app.route('/resume.html')
def resume():
    return send_from_directory('.', 'resume.html')

@app.route('/contact')
@app.route('/contact.html')
def contact():
    return send_from_directory('.', 'contact.html')

@app.route('/thankyou')
@app.route('/thankyou.html')
def thankyou():
    return send_from_directory('.', 'thankyou.html')

# Serve resume PDF if present
@app.route('/resume.pdf')
def resume_pdf():
    return send_from_directory('.', 'resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)
