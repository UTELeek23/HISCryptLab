from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os
# Khởi tạo SQLAlchemy và Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Khởi tạo Flask app
    app = Flask(__name__)
    if not os.path.exists('instance'):
        os.makedirs('instance')
    # Load cấu hình từ Config
    app.config.from_object(Config)

    # Khởi tạo SQLAlchemy và Migrate với app
    db.init_app(app)
    migrate.init_app(app, db)  # Khởi tạo Flask-Migrate
    from app import models
    # Tạo cơ sở dữ liệu và các bảng nếu chưa tồn tại
    with app.app_context():
        try:
            db.create_all()  # Tự động tạo các bảng từ model
            print("✅  Cơ sở dữ liệu được khởi tạo hoặc đã tồn tại.")
        except Exception as e:
            print(f"❌ Lỗi khi tạo cơ sở dữ liệu: {e}")

    # Đăng ký các blueprint
    try:
        from app.routes.main import main_bp
        from app.routes.auth import auth_bp
        from app.routes.challenges import challenges_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(challenges_bp)
        print("✅  Các blueprint đã được đăng ký thành công.")
    except ImportError as e:
        print(f"❌  Lỗi khi đăng ký blueprint: {e}")

    return app