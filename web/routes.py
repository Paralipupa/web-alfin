import os, pathlib, re
from faulthandler import disable
from genericpath import isdir
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from shutil import rmtree
from flask import render_template, flash, redirect, request, send_from_directory
from web import app
from web.forms import UploadForm
from alfin.module.calculate import Calc
from .settings import *


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    form = UploadForm()
    if request.method == 'POST': # and form.validate_on_submit():
        return __report(form.is_archi.data)
    return render_template('upload.html', title='Отчеты', form=form)

def __report(is_archi: bool = False):
    files = __upload_file()
    if files:
        report = Calc(files, is_archi)        
        return __download_file(report.run())
    return redirect('/')

def __upload_file() -> str:
    files = []
    if request.files:        
        os.makedirs(app.config['UPLOAD_DIR'], exist_ok=True)
        for name in request.files:
            file = request.files[name]
            if file.filename:
                filename = pathlib.Path(
                    app.config['UPLOAD_DIR'], secure_filename(f'{name}_{file.filename}'))
                file.save(filename)
                files.append(str(filename))
    return files

def __download_file(filename: str):
    return send_from_directory(os.path.dirname(filename), os.path.basename(filename), as_attachment=True)

