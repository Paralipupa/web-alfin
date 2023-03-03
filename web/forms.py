from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UploadForm(FlaskForm):
    datafile58WA = FileField('файл из 1С сч.58.03(ср.вз.)  ', validators=[DataRequired()])
    datafile58RES = FileField('файл из 1С сч.58.03(резерв) ', validators=[DataRequired()])
    datafile76 = FileField('файл из 1С сч.сч.76   ', validators=[DataRequired()])
    datafilePDN = FileField('файл c ПДН клиентов   ', validators=[DataRequired()])
    datafileIRKOM = FileField('файл выгрузки (Ирком)', validators=[DataRequired()])
    is_archi = BooleanField('данные из Archicredit (ставка,тариф,срок)')
    submit = SubmitField('Резервы')
