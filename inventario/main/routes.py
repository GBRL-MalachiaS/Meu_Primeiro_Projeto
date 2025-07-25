# meu_projeto/main/routes.py
from flask import render_template, Blueprint

# Criamos o objeto Blueprint
main = Blueprint('main', __name__)

# As rotas agora são associadas ao blueprint 'main', não mais ao 'app'
@main.route("/")
@main.route("/home")
def home():
    # A lógica da sua página inicial iria aqui
    return render_template('base.html')