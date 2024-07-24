from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from sqlalchemy.testing.pickleable import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import secrets

# Create a secrets token
secret = secrets.token_urlsafe(32)

# Create a flask application
app = Flask(__name__)
# Set the secret token to some random bytes. Keep this really secret!
app.secret_key = secret

# Tells flask-sqlalchemy what database to connect to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskproject.db'

# Initialize flask-sqlalchemy extension
db = SQLAlchemy(app)

# LoginManager is needed for our application
# to be able to log in and out users
login_manager = LoginManager()
login_manager.init_app(app)


# Create user model
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)


# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


# If the user made a POST request, create a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if not request.form.get('username'):
            flash('Username is required!')
            return redirect(url_for('register'))
        if not request.form.get('password'):
            flash('Password is required!')
            return redirect(url_for('register'))
        username = request.form['username']
        password = request.form['password']
        if Users.query.filter_by(username=username).first():
            flash('Username already exists!')
            return redirect(url_for('register'))
        user = Users(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template("sign_up.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'username' not in request.form or 'password' not in request.form:
            flash('Username and password are required!')
            return redirect(url_for('login'))
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(user)
        flash('Login successful!')
        next_page = request.args.get('next')
        return redirect(next_page or url_for('home'))
    return render_template('login.html')


@app.route('/logout')
# @login_required
def logout():
    logout_user()
    flash('Logout successful!')
    return redirect(url_for('home'))


@app.route("/")
def home():
    # Render home.html on "/" route
    return render_template("home.html")


# создаем поля в БД
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        post = Post(title=title, text=text)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/posts')
        except:
            return 'При добавлении заявки произошла ошибка'
    else:
        return render_template('create.html')


@app.route('/about')
def about():
    return render_template('about.html')  # '<h1>Страница о нас</h1>'


if __name__ == '__main__':
    app.run(debug=True)
