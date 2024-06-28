from flask import Flask, render_template, request, send_from_directory, url_for
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    # List .nii.gz files in the src directory
    src_folder = 'src'
    files = [f for f in os.listdir(src_folder) if f.endswith('.nii.gz')]
    return render_template('index.html', files=files)

@app.route('/view')
def view():
    file_name = request.args.get('filename')  # Adjust to match the name in your form
    if file_name:
        return render_template('view.html', file_name=file_name)
    return "File not found", 404

@app.route('/src/<filename>')
def serve_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'src'), filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
