from flask import *
from fileinput import filename
from pdfc import pdf_compressor
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = 'data'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/upload_file', methods = ['POST'])   
def upload_file():   
    if request.method == 'POST':   
        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file'] 
        
        if file.filename == '':
            return('No selected file')

        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            input_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            output_filename = os.path.join(app.config['UPLOAD_FOLDER'], "min_"+filename)
            power = 0
            # if filesize is greater than 20 MB use level-3 compression
            if (os.path.getsize(input_filename) >> 20) > 20:
                power = 3
            pdf_compressor.compress(input_filename,
                                        output_filename, power=power)
            return redirect(url_for('download_file', name="min_"+filename))

        else:
            return("Only PDF files are allowed!")
            # flash('No selected file')
            # return redirect(request.url)

@app.route('/download_file/<name>')
def download_file(name): 
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)