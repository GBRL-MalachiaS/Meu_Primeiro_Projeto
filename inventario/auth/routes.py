from flask import render_template, Blueprint
from inventario.auth.forms import FormLogin

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(username=form.usuario.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form.senha.data):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            
            return render_template('dashboard.html', user=usuario)
        else:
            # Logic for failed login
            form.usuario.errors.append('Usuário ou senha inválidos')
    return render_template('login.html', form=form)


@auth.route('/registro')
def registro():
    form = FormRegistro()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        
        # Here you would typically check if the username or email already exists
        # and create a new user if everything is valid.
        
        new_user = Usuario(username=username, email=email, password=password)
        # Save new_user to the database
    # Logic for user registration
    return render_template('registro.html')


@auth.route('/logout')
def logout():
    # Logic for logging out the user
    return render_template('logout.html')




@auth.route('/registro')
def registro():
    form = FormRegistro()
    
    print("URL Gerada:", url_for('auth.static', filename='css/registro.css'))
    if form.validate_on_submit():
        ...
    
    return render_template('registro.html', form=form)