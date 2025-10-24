from flask import Flask, render_template, request, redirect, url_for
import os
import DAL

app = Flask(__name__, static_folder='images', static_url_path='/images')

# Initialize the database
DAL.init_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    all_projects = DAL.get_all_projects()
    return render_template('projects.html', projects=all_projects)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    if request.method == 'POST':
        form_type = request.form.get('form_type', '')
        
        # Check if this is a project submission
        if form_type == 'project':
            title = request.form.get('title')
            description = request.form.get('description')
            image_filename = request.form.get('image_filename', '')
            
            # Add the project to the database
            DAL.add_project(title, description, image_filename)
            
            # Redirect to projects page to see the new project
            return redirect(url_for('projects'))
        
        # If not a project form, it's a contact form - could handle contact form here
        # For now, just redirect to thank you page
        return redirect(url_for('thankyou'))
    
    return render_template('forms.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
