from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UploadForm(FlaskForm):
    datafile58 = FileField('файл из 1С сч.58.03(ср.вз.)  ', validators=[DataRequired()])
    datafile58PDN = FileField('файл из 1С сч.58.03(ПДН) ', validators=[DataRequired()])
    datafile76 = FileField('файл из 1С сч.сч.76   ', validators=[DataRequired()])
    datafilePDN = FileField('файл c ПДН клиентов   ', validators=[DataRequired()])
    datafileIRKOM = FileField('файл выгрузки (Ирком)', validators=[DataRequired()])
    submit = SubmitField('Пуск')
