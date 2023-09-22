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

from models.course import Course
from routes import users


@app.route('/')
def hello_world():
    rec = db.get_or_404(Course, 1)
    return render_template('index.html', user=rec)


@app.route('/courses')
def courses():
    course= db.session.query(Course).all()
    courses = list(map(lambda rec: rec.__dict__, course))
    return render_template('courses.html', courses=courses)

     