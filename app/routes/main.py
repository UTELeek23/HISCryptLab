from flask import Blueprint, render_template

# Tạo một Blueprint cho các route chính
main_bp = Blueprint('main', __name__)

# Route cho trang chủ
@main_bp.route('/')
def home():
    return render_template('base.html')

# Route cho trang giới thiệu
@main_bp.route('/about')
def about():
    return render_template('about.html')

# Route cho trang liên hệ
@main_bp.route('/contact')
def contact():
    return render_template('contact.html')