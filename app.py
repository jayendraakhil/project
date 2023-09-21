from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, flash
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

class Contacts(db.Model):
    '''
    sno, name, phone_num, Subject,  email, timestamp
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(10), nullable=False)
    Subject = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Loginn(db.Model):
    '''
    sno,username,password,timestamp
    '''
    sno = db.Column(db.Integer, primary_key=True )
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Salt(db.Model):
    '''
    email,salt
    '''
    email = db.Column(db.String(50), primary_key=True)
    salt = db.Column(db.String(200), nullable=False)

class Signup(db.Model):
    '''
    email,password,repeatpassword,timestamp
    '''
    email = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    confirm_password=db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    


class Booki(db.Model):
    '''
    sno,name,email,phone,date_and_time,timestamp
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Bookiv(db.Model):
    '''
    sno,name,email,phone,date_and_time,timestamp
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Bookib(db.Model):
    '''
    sno,name,email,phone,date_and_time,timestamp
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
@app.route("/")
def home():
    app.logger.info('Homepage accessed.')
    return render_template("index4.html")


@app.route('/bed')
def bed():
    return render_template('bed.html')

@app.route('/couch')
def couch():
    return render_template('couch.html')

@app.route('/cupb')
def cupb():
    return render_template('cupb.html')

@app.route('/dt')
def dt():
    return render_template('dt.html')

@app.route('/studytb')
def studytb():
    return render_template('studytb.html')

@app.route('/sofa')
def sofa():
    return render_template('sofa.html')

# @app.route("/")
# def home1():
#     app.logger.info('Homepage 1 accessed.')
#     return render_template("index3.html")

@app.route("/index2")
def home2():
    app.logger.info('Homepage 2 accessed.')
    return render_template("index2.html")


@app.route("/about")
def about():
    app.logger.info('About page accessed.')
    return render_template("about.html")


@app.route('/books')
def books():
    return render_template('books.html')
# @app.route("/about1")
# def about1():
#     app.logger.info('About page 1 accessed.')
#     return render_template("about1.html")

# @app.route("/about2")
# def about2():
#     app.logger.info('About page 2 accessed.')
#     return render_template("about2.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        Subject = request.form.get('Subject')
        timestamp = datetime.datetime.now()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address entered.')
            return redirect(url_for('contact'))

        phone_regex = r'^\d{10,12}$'
        if not re.match(phone_regex, phone):
            error = "Phone number must be between 10 and 12 digits."
            flash('Invalid Phone Number entered.')
            return redirect(url_for('contact'))

        entry = Contacts(name=name, phone_num=phone, Subject=Subject, email=email,timestamp=timestamp)
        db.session.add(entry)
        db.session.commit()
        flash('Our team will reach out to you')
        return redirect(url_for('contact'))
    app.logger.info("contact page accessed")
    return render_template("contact.html")


# @app.route("/contact1", methods=['GET', 'POST'])
# def contact1():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         Subject = request.form.get('Subject')
#         timestamp = datetime.datetime.now()

#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             app.logger.error('Invalid email address entered.')
#             return "Invalid email address. Please try again."

#         phone_regex = r'^\d{10,12}$'
#         if not re.match(phone_regex, phone):
#             error = "Phone number must be between 10 and 12 digits."
#             app.logger.error('Invalid Phone Number entered.')
#             return "Invalid Phone Number. Please try again."
#         entry = Contacts(name=name, phone_num=phone, Subject=Subject, email=email,timestamp=timestamp)
#         db.session.add(entry)
#         db.session.commit()
#         app.logger.info('Our team will reach out to you')
#         return "Our team will reach out to you"
#     app.logger.info("contact 1 page accessed")
#     return render_template("contact1.html")

 

# @app.route("/contact2", methods=['GET', 'POST'])
# def contact2():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         Subject = request.form.get('Subject')
#         timestamp = datetime.datetime.now()

#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             app.logger.error('Invalid email address entered.')
#             return "Invalid email address. Please try again."

#         phone_regex = r'^\d{10,12}$'
#         if not re.match(phone_regex, phone):
#             error = "Phone number must be between 10 and 12 digits."
#             app.logger.error('Invalid Phone Number entered.')
#             return "Invalid Phone Number. Please try again."

#         entry = Contacts(name=name, phone_num=phone, Subject=Subject, email=email,timestamp=timestamp)
#         db.session.add(entry)
#         db.session.commit()
#         app.logger("Contact entry added successfully")
#         return "Our team will reach out to you"
#     app.logger.info("Our team will reach out to you")
#     return render_template("contact2.html")




@app.route("/login_form", methods=['GET', 'POST'])
def logg():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get("password")
        timestamp = datetime.datetime.now()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address entered.')
            return redirect(url_for('logg')) 
        
        user = Signup.query.filter_by(email=email).first()
        if not user:
            flash('Invalid username or password entered.')
            return redirect(url_for('logg')) 
        hashed = bcrypt.hashpw(password.encode('utf-8'), mask.mask)
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        
            entry = Loginn(email=email, password=hashed,timestamp=timestamp)
            db.session.add(entry)  
            db.session.commit()
            salt_entry = Salt.query.filter_by(email=email).first()
            if salt_entry:
                salt = salt_entry.salt
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8')
                user = Signup.query.filter_by(email=email, password=hashed_password).first()
                if user:
                    flash('User has successfully logged in.')
                    return render_template('index2.html', ans="Logged in successfully.")
                else:
                    flash('Salt entry not found for the given user.')
                    return redirect(url_for('logg')) 
    app.logger.info("login page accessed")
    return render_template('login_form.html')
    


@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        timestamp = datetime.datetime.now()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address. Please try again.', 'error')
            return render_template('sign_up.html')

        if password != confirm_password:
            flash('Password and Confirm Password do not match. Please try again.', 'error')
            return render_template('sign_up.html')

        salt = bcrypt.gensalt().decode('utf-8')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8')

        user = Signup.query.filter_by(email=email).first()
        if user:
            flash('User already exists. Please log in.', 'error')
            return render_template('sign_up.html')

        entry = Signup(email=email, password=hashed_password, confirm_password=confirm_password,timestamp=timestamp)
        db.session.add(entry)
        db.session.commit()

        salt_entry = Salt(email=email, salt=salt)
        db.session.add(salt_entry)
        db.session.commit()

        flash('User signed up successfully.', 'success')
        return render_template('login_form.html')
    else:
        return render_template('sign_up.html')




if __name__ == '__main__':
    with app.app_context():

        db.create_all()
        app.run(debug=True)
