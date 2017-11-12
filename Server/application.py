from flask import Flask
from flask import render_template
from flask import request, url_for, redirect
import os
from werkzeug import secure_filename
from flask_wtf.file import FileField


IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/uploads', methods=['GET','POST'])
def uploads():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return(render_template("uploads.html"))
    return render_template('uploads.html')


@app.route('/Cheeseit', methods=['GET','POST'])
def cheese():
    return render_template('Cheeseit.html')
