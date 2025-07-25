from flask import render_template, Blueprint
from inventario.auth.forms import FormLogin

auth = Blueprint('auth', __name__, template_folder='templates')



@auth.route('/login')
def login():
    form = FormLogin()
    
    if form.validate_on_submit():
        ...
    return render_template('login.html', form=form)
