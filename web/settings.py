from werkzeug.security import generate_password_hash
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "oksana": generate_password_hash("javajas345"),
}
