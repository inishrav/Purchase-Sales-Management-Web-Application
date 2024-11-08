# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# here i am going to integrate the sql in flask because
# here we are having some database tables with some fields they are company, item, purchase, sales

# below i am having the primary key and also foreign key because the item_id is repeated again and again and also it is referring from before table
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    # every time i want to report the current cash balance so i am giving as 
    cash_balance = db.Column(db.Float, default=1000.0)  # here the initial cash_balance is 1000

# next i am going to create a db model for item   
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    rate = db.Column(db.Float, nullable=False)  # here i am adding the quantity column in a Item table and initially i am keeping that as default 0
    # if they are purchasing i am going to add the quantity and if they are selling i am going to reduce the quantity
    qty = db.Column(db.Integer, default=0)

# i am going to create a Purchase db model 
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # here in am having the foreign key ->item_id because it is referring before the data model
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)

# to create a tables
with app.app_context():
    db.create_all()  
    if not Company.query.first():  # Check if any company exists
        default_company = Company(name='Default Company', cash_balance=1000.0)
        db.session.add(default_company)
        db.session.commit()

# now i have to create a views for Item, Purchases and  for Sales
@app.route('/')
def index():
    company = Company.query.first()
    return render_template('index.html', balance=company.cash_balance)

@app.route('/items', methods=['GET', 'POST'])
def managing_items():
    if request.method == 'POST':
        # adding a new item with name and rate
        name = request.form['name']
        rate = request.form['rate']
        item = Item(name=name, rate=rate)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('managing_items'))
    items = Item.query.all()
    return render_template('items.html', items=items)

# New route to delete an item
@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('managing_items'))

@app.route('/purchase', methods=['GET', 'POST'])
def add_purchase():
    if request.method == 'POST':
        item_id = request.form['item_id']
        qty = int(request.form['qty'])
        rate = float(request.form['rate'])
        amount = qty * rate
        purchase = Purchase(item_id=item_id, qty=qty, rate=rate, amount=amount)
        
        # Update item quantity and company balance
        item = Item.query.get(item_id)
        item.qty += qty  # here if they are purchasing i am going to add the quantity so i am updating here
        company = Company.query.first()
        company.cash_balance -= amount  # above it will display the purchase cost

        db.session.add(purchase)
        db.session.commit()
        return redirect(url_for('add_purchase'))

    items = Item.query.all()
    return render_template('purchases.html', items=items)

@app.route('/sales', methods=['GET', 'POST'])
def add_sale():
    if request.method == 'POST':
        item_id = request.form['item_id']
        qty = int(request.form['qty'])
        rate = float(request.form['rate'])
        amount = qty * rate
        sale = Sale(item_id=item_id, qty=qty, rate=rate, amount=amount)
        
        # Update item quantity and company balance
        item = Item.query.get(item_id)
        item.qty -= qty  # deduct sold quantity from stock
        company = Company.query.first()
        company.cash_balance += amount  # above it will display the purchase cost

        db.session.add(sale)
        db.session.commit()
        return redirect(url_for('add_sale'))

    items = Item.query.all()
    return render_template('sales.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
