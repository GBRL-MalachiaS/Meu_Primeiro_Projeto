from flask import render_template, Blueprint, url_for, redirect, flash
from flask_login import login_user, current_user, logout_user, login_required
from inventario import db, bcrypt
from inventario.models import Usuario
from inventario.auth.forms import FormLogin, FormRegistro


auth = Blueprint(
    'auth', __name__,
    template_folder='templates',
    static_folder='static')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = FormLogin()

    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(usuario=form.usuario.data).first()

        if usuario and bcrypt.check_password_hash(usuario.password, form.senha.data):
            login_user(usuario, remember=form.lembrar_dados.data)
            flash()
            return redirect(url_for('main.home'))
        else:
            flash('Falha ao efetuar login. Valide seu usuário e senha', 'danger')
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@auth.route('/registro', methods=['GET', 'POST'])
def registro():
    form = FormRegistro()

    if form.validate_on_submit():
        senha_hash = bcrypt.generate_password_hash(
            form.senha.data).decode('utf-8')
        novo_usuario = Usuario(
            usuario=form.usuario.data,
            nome_completo=form.nome_completo.data,
            email=form.email.data,
            password=senha_hash
        )
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Sua conta foi criada')
        return redirect(url_for('auth.login'))
    return render_template('registro.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado com sucesso.', 'info')
    return redirect(url_for('auth.login'))


@auth.route('/alterarsenha')
def alterar_senha():
    
    return render_template('alterarsenha.html')