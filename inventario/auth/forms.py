from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from .validators import validate_email,validate_senha,validate_usuario


class FormLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo usuarío é obrigatório')])
    senha = PasswordField('Senha', validators=[
        DataRequired(message='Campo senha é obrigatório')])
    enviar = SubmitField('Fazer Login')


class FormRegistro(FlaskForm):
    usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo Obrigatório'),
        Length(min=8, message='Campo deve ter 8 digitos'),
        validate_usuario,
        ])
    
    nome_completo = StringField('Nome Completo', validators=[
        DataRequired(message='Campo Obrigatório')
    ])
    
    email = EmailField('E-mail', validators=[
        DataRequired(message='Por favor, ensira seu e-mail'),
        Email(message='Digite um e-mail valido'),
        validate_email,
        ])

    senha = PasswordField('Senha', validators=[
        DataRequired(message='Campo Obrigatório'),
        Length(min=12, message='Campo deve ter no minimo 12 caracteres'), 
        validate_senha
    ])
    confirmar_senha = PasswordField('Confirmar a senha', validators=[
        DataRequired(message='Campo Obrigatório'),
        Length(min=12),
        EqualTo('senha', message='As senhas devem ser iguais'),
    ])

    enviar = SubmitField('Cadastrar')

class FormAlterarSenha(FlaskForm):
    senha = PasswordField('Senha', validators=[DataRequired('Campo Obrigatório')])