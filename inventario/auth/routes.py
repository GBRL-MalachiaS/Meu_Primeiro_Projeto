from flask import render_template, Blueprint, url_for, redirect
from inventario.auth.forms import FormLogin, FormRegistro

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    
    if form.validate_on_submit():
        ...
    return render_template('login.html', form=form)

@auth.route('/registro')
def registro():
    form = FormRegistro()
    
    print("URL Gerada:", url_for('auth.static', filename='css/registro.css'))
    if form.validate_on_submit():
        ...
    
    return render_template('registro.html', form=form)

@auth.route('/logout')
def logout():
    # Logic for logging out the user
    return render_template('logout.html')

