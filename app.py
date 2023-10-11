import os
from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
app = Flask(__name__)
app.logger.setLevel('INFO')
Bootstrap(app)

host = os.environ.get('SALES_DB_HOST')
port = os.environ.get('SALES_DB_PORT')
db_name = os.environ.get('SALES_DB_NAME')
user = os.environ.get('SALES_DB_USER')
password = os.environ.get('SALES_DB_PASS')
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
app.config['SQLALCHEMY_ECHO'] = eval(os.environ.get('LOG_SQL_QUERIES','FALSE'))
db.init_app(app)

from models.user import User
from models.course import Course

 
from routes import users
from routes import courses
 


@app.route('/')
def hello_world():
     
    return redirect(url_for('users'))


 

     