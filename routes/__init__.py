"""
Routes package for ANPR-based vehicle tracking system.

This package contains all the route handlers for the application:
- auth.py: Authentication routes (login, register, logout)
- admin.py: Admin panel routes (vehicle management, user management)
- security.py: Security officer routes (vehicle scanning)
- dashboard.py: Dashboard and statistics routes
"""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    return render_template('welcome.html')
