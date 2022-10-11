import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lsadpo2304980nsljfo8475hkfjhbjh #%%^%$^52 khj'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_DIR = 'upload'
    DOWNLOAD_DIR = 'output'