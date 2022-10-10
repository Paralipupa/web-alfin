import os
from faulthandler import disable
from genericpath import isdir
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from shutil import rmtree
from flask import render_template, flash, redirect, request, send_from_directory
from web import app
from web.forms import LoginForm, UploadForm
# from ..parsers.module.parser import Parser
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
    if request.method == 'POST' and form.validate_on_submit():
        return __parser()
    return render_template('upload.html', title='Парсер', form=form)


@app.route('/convert', methods=['POST'])
@auth.login_required
def convert():
    inn = request.form.to_dict().get('inn')
    if not inn:
        inn = request.args.get('inn')
    return __parser(inn)


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
@auth.login_required
def download(filename):
    return __download_file(filename)


@app.route('/remove/<path:pathname>', methods=['GET'])
@auth.login_required
def remove(pathname):
    path = __get_files(pathname)
    if path:
        flash('Папка {} удалена'.format(path))
        __remove_files(path)
    return redirect('/')


@app.route('/list/<path:pathname>', methods=['GET'])
@auth.login_required
def list(pathname):
    if isinstance(pathname, str): 
        path = __get_files(pathname)
        if path:
            return __list_files(path)
    return pathname


def __parser():
    filename = __upload_file()
    if filename:
        parser = Parser(file_name=filename, inn=inn,
                        path_down=app.config['DOWNLOAD_DIR'])
        file_zip = parser.start()
        if file_zip:
            return __download_file(file_zip)
    return redirect('/')


def __upload_file() -> str:
    if request.files and 'datafile' in request.files:
        file = request.files['datafile']
        filename = os.path.join(
            app.config['UPLOAD_DIR'], secure_filename(file.filename))
        os.makedirs(app.config['UPLOAD_DIR'], exist_ok=True)
        file.save(filename)
        return filename
    return ''


def __download_file(filename: str):
    return send_from_directory(str(os.path.join(app.config['BASE_DIR'], app.config['DOWNLOAD_DIR'])), str(filename), as_attachment=True)


def __remove_files(path: str):
    if os.path.isdir(path):
        rmtree(path)


def __list_files(path: str):
    if os.path.isdir(path):
        return list(map(__to_str, (os.path.join(path, f) for f in os.listdir(path))))


def __get_files(pathname: str) -> str:
    path = ''
    if pathname == 'download':
        path = app.config['DOWNLOAD_DIR']
    elif pathname == 'upload':
        path = app.config['UPLOAD_DIR']
    # else:
    #     path = Parser.get_path(pathname)
    if path and not os.path.isdir(path):
        path = ''
    return path

def __to_str(val:str)->str:
    return f'{val}; '
