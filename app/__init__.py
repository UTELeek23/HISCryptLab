from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Đăng ký các blueprint
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.challenges import challenges_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(challenges_bp)

    return app