from flask import render_template, flash, redirect, request
from wtforms import Form, StringField, TextField, TextAreaField, validators, PasswordField, BooleanField, SubmitField
from app import app
from boto.dynamodb2.layer1 import DynamoDBConnection
from app.dynam import dynam

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
  
    if request.method == 'POST':
        Zipcode=request.form['Zipcode']
        Cuisine=request.form['Cuisine']
        Price=request.form['Price']
        Rating=request.form['Zipcode']
        delivery=request.form['delivery']
        deliveryNow=request.form['deliveryNow']

        a = dynam()
        #a.create()

        a.putItems()


    return render_template('index.html', form=form)

