from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/index')
def index():
    return render_template('index.html')

# Configure MySQL connection
db_config = {
    'host': 'localhost',  # Change this to your MySQL host
    'user': 'root',  # Your MySQL username
    'password': 'root',  # Your MySQL password
    'database': 'suspect_finder.db'  # Your MySQL database name
}

# Folder to store uploaded images
UPLOAD_FOLDER = 'uploads/suspect_images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions for image upload
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'jfif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/try', methods=['GET', 'POST'])
def suspect_form():  # Changed function name to avoid conflict
    if request.method == 'POST':
        # Get form data
        suspect_name = request.form['suspect_name']
        crime_details = request.form['crime_details']
        suspect_details = request.form['suspect_details']

        # Handle file upload
        if 'suspect_image' not in request.files:
            return "No file part", 400

        file = request.files['suspect_image']
        
        if file.filename == '':
            return "No selected file", 400
        
        if file and allowed_file(file.filename):
            # Secure file name and save the file
            filename = suspect_name.replace(" ", "_") + '.' + file.filename.rsplit('.', 1)[1].lower()
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Connect to the database
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            # Insert suspect details into the `suspects` table
            cursor.execute(""" 
                INSERT INTO suspects (suspect_name, crime_details, suspect_details)
                VALUES (%s, %s, %s)
            """, (suspect_name, crime_details, suspect_details))
            
            # Get the last inserted suspect_id
            suspect_id = cursor.lastrowid
            
            # Insert image details into the `suspect_images` table
            cursor.execute(""" 
                INSERT INTO suspect_images (suspect_id, image_path)
                VALUES (%s, %s)
            """, (suspect_id, file_path))
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return "Suspect details and image uploaded successfully!", 200
        else:
            return "Invalid file type. Only jpg, jpeg, png, jfif files are allowed.", 400

    return render_template('try.html')

if __name__ == '__main__':
    app.run(debug=True)
