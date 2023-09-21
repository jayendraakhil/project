from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import datetime
import bcrypt
import re
import mask as mask
import logging

app = Flask(__name__)
app.secret_key = 'my_secret_key'
# logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
dbname = 'postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:1234@localhost:5432/postgres'
#app.config['SQLALCHEMY_DATABASE_URL'] = 'postgres://username:password@localhost:5432/dbname'

db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)  





@app.route("/")
def home():
    app.logger.info('Homepage accessed.')
    return render_template("test.html")

@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = Admin.query.filter_by(username=username).first()

        if admin and bcrypt.checkpw(password.encode('utf-8'), admin.password.encode('utf-8')):
            # Admin is authenticated, set a session variable or a cookie to track admin status
            session['admin_logged_in'] = True
            flash('Admin logged in successfully', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('admin_users.html')



if __name__ == '__main__':
    with app.app_context():

        db.create_all()
        app.run(debug=True)
