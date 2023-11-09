import os, pathlib, re
from wtforms import DateField
from datetime import datetime
from faulthandler import disable
from genericpath import isdir
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from shutil import rmtree
from flask import render_template, flash, redirect, request, send_from_directory
from web import app
from web.forms import UploadForm
from alfin.module.calculate_async import Calc
from .settings import *


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    form : UploadForm = UploadForm()
    if request.method == 'POST': # and form.validate_on_submit():
        options = __get_options(form)
        return __report(form.date_purpose, **options)
    return render_template('upload_multi.html', title='Отчеты', form=form, files = request.files)

def __get_options(form) -> dict:
    names = [a for a in dir(form) if a.startswith('option_')]
    options = dict()
    for name in names:
        options.setdefault(name, vars(form)[name].data)
    return options

def __report(date_purpose: DateField, **options):
    files = __upload_file()
    if files:
        if date_purpose.raw_data[0]:
            date_p = datetime.strptime(date_purpose.raw_data[0],"%Y-%m-%d").date()
        else:
            date_p = None            
        report = Calc(files,  date_p, **options)
        return __download_file(report.run())
    return redirect('/')

def __upload_file() -> str:
    files = []
    if request.files:
        os.makedirs(app.config['UPLOAD_DIR'], exist_ok=True)
        for index, file in enumerate(request.files.getlist('file')):
            if file.filename:
                filename = pathlib.Path(
                    app.config['UPLOAD_DIR'], secure_filename(f'{index}_{file.filename}'))
                file.save(filename)
                files.append(str(filename))
    return files

def __download_file(filename: str):
    if filename is None:
        return redirect('/')
    return send_from_directory(os.path.dirname(filename), os.path.basename(filename), as_attachment=True)

