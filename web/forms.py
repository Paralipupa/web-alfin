from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UploadForm(FlaskForm):
    datafile58WA = FileField('сч.58.03', validators=[DataRequired()])
    datafile58RES = FileField('', validators=[DataRequired()])
    datafile76 = FileField('', validators=[DataRequired()])
    datafilePDN = FileField('', validators=[DataRequired()])
    datafileIRKOM = FileField('', validators=[DataRequired()])
    date_purpose = DateField('дата начисления', format='%d.%m.%Y' )
    option_is_archi = BooleanField('данные из Archicredit (ставка,тариф,срок)', default=True)
    option_clients = BooleanField('сред.взвешеная', default=False)
    option_weighted_average = BooleanField('сред.взвешеная', default=False)
    option_kategory = BooleanField('категория', default=False)
    option_reserve = BooleanField('резервы', default=False)
    option_handle = BooleanField('операции вручную', default=False)
    option_cb_common = BooleanField('ЦБ (общий)', default=False)
    option_cb_kassa = BooleanField('ЦБ (касса)', default=False)
    option_cb_rs = BooleanField('ЦБ (р/с)', default=False)
    submit = SubmitField('Запуск')
