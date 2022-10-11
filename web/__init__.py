import sys
from flask import Flask

from config import Config

sys.path.append('alfin')
app = Flask(__name__)
app.config.from_object(Config)

from web import routes