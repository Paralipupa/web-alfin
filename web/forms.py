from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UploadForm(FlaskForm):
    # inn = StringField('ИНН')
    datafile58 = FileField('сч.58   ', validators=[DataRequired()])
    datafile76 = FileField('сч.76   ', validators=[DataRequired()])
    datafilePDN = FileField('PDN   ', validators=[DataRequired()])
    datafileIRKOM = FileField('IRKOM', validators=[DataRequired()])
    submit = SubmitField('Пуск')
