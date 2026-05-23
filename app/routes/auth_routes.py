from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.models.usuario import Usuario
from app import db

auth_bp = Blueprint('auth', __name__)


# HOME
@auth_bp.route('/')
def home():

    return render_template('home.html')


# LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and usuario.check_password(password):

            login_user(usuario)

            return redirect(url_for('auth.dashboard'))

        flash('Usuario o contraseña incorrectos')

    return render_template('auth/login.html')


# REGISTRO
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        nuevo_usuario = Usuario(
            username=username
        )

        nuevo_usuario.set_password(password)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Usuario registrado correctamente')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


# DASHBOARD
@auth_bp.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')


# LOGOUT
@auth_bp.route('/logout')
def logout():

    logout_user()

    return redirect(url_for('auth.login'))