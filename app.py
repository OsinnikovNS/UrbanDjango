from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskproject.db'
db = SQLAlchemy(app)

# создаем поля в БД
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' %self.id

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        print(request.form[title])
        print(request.form[text])
    else:
        return render_template('create.html')


@app.route('/about')
def about():
    return render_template('about.html')  # '<h1>Страница о нас</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Привет, %s!</h1>' %name

if __name__ == '__main__':
    app.run(debug=True)
