from flask import Flask, render_template, request, redirect, url_for, flash, g
import os
from test import FaceMatchingSystem  # Import your existing code

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Ensure upload directories exist
UPLOAD_FOLDER_REAL = os.path.join('static', 'uploads', 'real_images')
UPLOAD_FOLDER_SKETCH = os.path.join('static', 'uploads', 'sketch')
os.makedirs(UPLOAD_FOLDER_REAL, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_SKETCH, exist_ok=True)

app.config['UPLOAD_FOLDER_REAL'] = UPLOAD_FOLDER_REAL
app.config['UPLOAD_FOLDER_SKETCH'] = UPLOAD_FOLDER_SKETCH

DATABASE_PATH = 'face_database.db'

# --- SQLite Per-Request Connection ---
def get_face_matching_system():
    if 'face_system' not in g:
        g.face_system = FaceMatchingSystem(DATABASE_PATH)
    return g.face_system

@app.teardown_appcontext
def close_connection(exception):
    face_system = g.pop('face_system', None)
    if face_system is not None:
        face_system.close_connection()
# --------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    # Handle real images upload
    real_images = request.files.getlist('real_images')
    for image in real_images:
        if image:
            image.save(os.path.join(app.config['UPLOAD_FOLDER_REAL'], image.filename))
    
    # Handle sketch upload
    sketch = request.files.get('sketch')
    if sketch:
        sketch_path = os.path.join(app.config['UPLOAD_FOLDER_SKETCH'], sketch.filename)
        sketch.save(sketch_path)
    else:
        flash('Please upload a sketch image.')
        return redirect(url_for('index'))
    
    # Load real images into the database
    face_system = get_face_matching_system()
    face_system.load_images_to_database(app.config['UPLOAD_FOLDER_REAL'])
    
    # Perform face matching
    matches = face_system.compare_faces(sketch_path)

    # Render results
    return render_template('index.html', matches=matches, sketch_path=sketch_path)

@app.route('/clear')
def clear_database():
    # Close database and remove the database file
    os.remove(DATABASE_PATH)
    flash('Database cleared!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
