# meu_projeto/main/routes.py
from flask import render_template, Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user

# Criamos o objeto Blueprint
main = Blueprint('main', __name__, template_folder='templates',static_folder='static')

# As rotas agora são associadas ao blueprint 'main', não mais ao 'app'
@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))


