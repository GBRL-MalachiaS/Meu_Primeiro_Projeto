from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo


class FormLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='Campo usuarío é obrigatório')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Campo senha é obrigatório')])
    enviar = SubmitField('Fazer Login')

