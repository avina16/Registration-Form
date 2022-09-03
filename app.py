from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class regforms(db.Model):
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email= db.Column(db.String(100) , primary_key=True)
    password= db.Column(db.String(50))
    acctype=db.Column(db.String(20))
    terms=db.Column(db.String(3), nullable=False)
    age=db.Column(db.Integer)
    referrer=db.Column(db.String(50))
    bio=db.Column(db.String(200))
    
    def __init__(self, firstname,lastname, email,password, acctype, terms, age, referrer, bio):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.acctype=acctype
        self.terms=terms
        self.age=age
        self.referrer=referrer
        self.bio= bio
   
@app.route('/')
def show_all():
   return render_template('show_all.html', regforms = regforms.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['firstname'] or not request.form['lastname'] or not request.form['email'] or not request.form['password']or not request.form['acctype']or not request.form['terms']or not request.form['age']or not request.form['referrer']or not request.form['bio']:
         flash('Please enter all the fields', 'error')
      else:
         regform = regforms(request.form['firstname'], request.form['lastname'],  request.form['email'], request.form['password'],request.form['acctype'], request.form['terms'], request.form['age'], request.form['referrer'], request.form['bio'])
         
         db.session.add(regform)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug = True)   
   
   
