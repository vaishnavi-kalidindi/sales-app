import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
app = Flask(__name__)
Bootstrap(app)

host = os.environ.get('SALES_DB_HOST')
port = os.environ.get('SALES_DB_PORT')
db_name = os.environ.get('SALES_DB_NAME')
user = os.environ.get('SALES_DB_USER')
password = os.environ.get('SALES_DB_PASS')
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
db.init_app(app)

<<<<<<< HEAD
from models.course import Course
from models.user import User
=======
 
from routes import users
from routes import courses
>>>>>>> 5a1f74cb99875fcfe9491a454660dd6898d879e7


@app.route('/')
def hello_world():
    rec = db.get_or_404(Course, 1)
    return render_template('index.html', user=rec)

@app.route('/users')
def users():
    user_recs = db.session.query(User).all()
    users = list(map(lambda rec: rec.__dict__, user_recs))
    return render_template('users.html', users=users)

 

     