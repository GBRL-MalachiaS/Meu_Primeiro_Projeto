from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo


class FormLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo usuarío é obrigatório')])
    senha = PasswordField('Senha', validators=[
        DataRequired(message='Campo senha é obrigatório')])
    enviar = SubmitField('Fazer Login')

class FormRegistro(FlaskForm):
    usuario = StringField('Usuário', validators=[
        DataRequired(message='Campo usuário é obrigatório'),
        Length(min=3, max=150, message='O usuário deve ter entre 3 e 150 caracteres')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Campo email é obrigatório'),
        Email(message='Email inválido')
    ])
    senha = PasswordField('Senha', validators=[
        DataRequired(message='Campo senha é obrigatório'),
        Length(min=6, message='A senha deve ter pelo menos 6 caracteres')
    ])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[
        DataRequired(message='Confirmação de senha é obrigatória'),
        EqualTo('password', message='As senhas devem coincidir')
    ])
    enviar = SubmitField('Registrar')

    def validate_usuario(self, usuario):
        # Logic to check if the username already exists
        pass

    def validate_email(self, email):
        # Logic to check if the email already exists
        pass