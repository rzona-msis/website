import sqlite3
import os

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), 'projects.db')

def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

def init_database():
    """Initialize the database and create the projects table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_filename TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_all_projects():
    """Retrieve all projects from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM projects ORDER BY created_at DESC')
    projects = cursor.fetchall()
    
    conn.close()
    return projects

def get_project_by_id(project_id):
    """Retrieve a single project by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
    project = cursor.fetchone()
    
    conn.close()
    return project

def insert_project(title, description, image_filename=None):
    """Insert a new project into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO projects (title, description, image_filename)
        VALUES (?, ?, ?)
    ''', (title, description, image_filename))
    
    conn.commit()
    project_id = cursor.lastrowid
    conn.close()
    
    return project_id

def update_project(project_id, title, description, image_filename=None):
    """Update an existing project."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE projects
        SET title = ?, description = ?, image_filename = ?
        WHERE id = ?
    ''', (title, description, image_filename, project_id))
    
    conn.commit()
    conn.close()

def delete_project(project_id):
    """Delete a project from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    
    conn.commit()
    conn.close()

# Initialize the database when this module is imported
if __name__ == '__main__':
    init_database()
    print("Database initialized successfully!")
