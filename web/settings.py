from werkzeug.security import generate_password_hash
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "robot-ui": generate_password_hash("raideff86reps$"),
}
