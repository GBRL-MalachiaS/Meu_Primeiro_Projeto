from inventario.models import Usuario
from wtforms.validators import ValidationError
import re


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
