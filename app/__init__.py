from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():

    app = Flask(__name__)

    # SECRET KEY
    app.config['SECRET_KEY'] = os.environ.get(
        'SECRET_KEY',
        'clinica'
    )

    # BASE DE DATOS
    database_url = os.environ.get('DATABASE_URL')

    if database_url:
        # Compatibilidad PostgreSQL Render
        if database_url.startswith("postgres://"):
            database_url = database_url.replace(
                "postgres://",
                "postgresql://",
                1
            )

        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # Local (tu PC)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.models.usuario import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # BLUEPRINTS
    from app.routes.medico_routes import medico_bp
    from app.routes.paciente_routes import paciente_bp
    from app.routes.consulta_routes import consulta_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.historial_routes import historial_bp
    from app.routes.reportes_routes import reportes_bp

    # REGISTER
    app.register_blueprint(medico_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(consulta_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(historial_bp)
    app.register_blueprint(reportes_bp)

    return app
