from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from inventario.models import Usuario
import re


class FormLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo usuarío é obrigatório')])
    senha = PasswordField('Senha', validators=[
        DataRequired(message='Campo senha é obrigatório')])
    usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo usuarío é obrigatório')])
    senha = PasswordField('Senha', validators=[
        DataRequired(message='Campo senha é obrigatório')])
    enviar = SubmitField('Fazer Login')


class FormRegistro(FlaskForm):
    usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo Obrigatório'),
        Length(min=8, message='Campo deve ter 8 digitos')])
    nome_completo = StringField('Nome Completo', validators=[
        DataRequired(message='Campo Obrigatório')
    ])
    email = EmailField('E-mail', validators=[
        DataRequired(message='Por favor, ensira seu e-mail'),
        Email(message='Digite um e-mail valido')])

    confirmar_email = EmailField('Confirmar  o e-mail', validators=[
        DataRequired(message='Ensira novamente seu e-mail'),
        EqualTo('email', message='Os e-mails devem ser iguais'),
        Email(message='Digite um e-mail valido!')])

    senha = PasswordField('Senha', validators=[
        DataRequired(message='Campo Obrigatório'),
        Length(min=12, message='Campo deve ter no minimo 12 caracteres')
    ])
    confirmar_senha = PasswordField('Confirmar a senha', validators=[
        DataRequired(message='Campo Obrigatório'),
        Length(min=12),
        EqualTo('senha', message='As senhas devem ser iguais'),
    ])

    enviar = SubmitField('Cadastrar')

    # Valida se o usuário ja foi cadastrado
    def validate_usuario(self, usuario):

        usuario_existe = Usuario.query.filter_by(usuario=usuario.data).first()
        if usuario_existe:
            raise ValidationError(
                'Este nome de usuário já está em uso. Por favor, escolha outro.')

    # Valida se já existe e-mail cadastrado
    def validate_email(self, email):

        email_existe = Usuario.query.filter_by(email=email.data).first()

        if email_existe:
            raise ValidationError(
                'Este e-mail já está cadastrado, por favor, escolha outro!')

    # Valida se o usuário digitou senha com caracter
    def validate_senha(self, senha):
        senha_texto = senha.data

        if not re.search(r'[^A-Za-z0-9]', senha_texto):
            raise ValidationError('A senha deve conter um caractere especial!')
