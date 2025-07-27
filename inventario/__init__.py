# meu_projeto/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from inventario.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'usuarios.login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    from inventario.models import Usuario
    return Usuario.query.get(int(user_id))


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Agora associamos as extensões à nossa instância 'app'
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Importa e registra os Blueprints
    from inventario.main.routes import main as main_blueprint
    from inventario.auth.routes import auth as auth_blueprint

    # Registro dos pacotes Blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app