from flask import Blueprint, render_template, url_for, request, redirect, flash, session
from flask_login import login_required, login_user, logout_user
from flask_login_app.models import User
from flask_login_app import db, bcrypt
from email_validator import validate_email, EmailNotValidError


auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.signin'))
        
        login_user(user)
        
        return redirect(url_for('main.index'))

    return render_template('signin.html')

@auth_blueprint.route('/signout')
@login_required
def signout():

    # ログアウト
    logout_user()

    return redirect(url_for('main.index'))

@auth_blueprint.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # 入力値をセッションに保持
        session['name'] = name
        session['email'] = email

        # メールアドレスのバリデーションを実施
        try:
            validate_email(email)
        except EmailNotValidError as e: 
            flash(str(e), 'error')
            return redirect(url_for('auth.signup'))

        # ユーザー存在確認
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Already registered")
            return redirect(url_for('auth.signup'))

        # ユーザーを作成
        new_user = User(name=name, email=email, password=bcrypt.generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        # 名前とメールアドレスをセッションから削除
        if 'name' in session:
            session.pop('name', None)
        
        if 'email' in session:
            session.pop('email', None)

        return redirect(url_for('auth.signin'))

    return render_template('signup.html', form_data=session)
