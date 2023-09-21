from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.secret_key = 'my_secret_key'

# Configure your database URI here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin_panel.db'
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)

# Create the database tables
with app.app_context():
    db.create_all()

# Create Flask-Admin instance
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

# Create admin view for the Product model
class ProductAdmin(ModelView):
    column_list = ['name', 'description', 'price']
    form_columns = ['name', 'description', 'price']

admin.add_view(ProductAdmin(Product, db.session))

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('ad.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
