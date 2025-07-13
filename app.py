from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    # Debug information
    print(f"Current working directory: {os.getcwd()}")
    print(f"Template folder: {app.template_folder}")
    print(f"Template folder exists: {os.path.exists(app.template_folder)}")
    
    # List all files in current directory
    print(f"Files in current directory: {os.listdir('.')}")
    
    # List files in template folder
    if os.path.exists(app.template_folder):
        print(f"Files in template folder: {os.listdir(app.template_folder)}")
    else:
        print("Template folder does not exist!")
    
    # Check if index.html exists
    index_path = os.path.join(app.template_folder, 'index.html')
    print(f"index.html path: {index_path}")
    print(f"index.html exists: {os.path.exists(index_path)}")
    
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering template: {e}")
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
