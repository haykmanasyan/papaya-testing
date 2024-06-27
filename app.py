from flask import Flask, render_template, request, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # List .nii.gz files in the src directory
    src_folder = 'src'
    files = [f for f in os.listdir(src_folder) if f.endswith('.nii.gz')]
    return render_template('index.html', files=files)

@app.route('/view')
def view():
    # Get the selected file from the query parameters
    file_name = request.args.get('file')
    if file_name:
        file_path = os.path.join('src', file_name)
        if os.path.exists(file_path):
            return render_template('view.html', file_name=file_name)
    return "File not found", 404

@app.route('/src/<filename>')
def serve_file(filename):
    return send_from_directory('src', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
