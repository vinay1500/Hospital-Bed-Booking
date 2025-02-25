from flask import Flask,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_required,logout_user,login_user,login_manager,LoginManager,current_user

# database connection

local_server = True
app =  Flask(__name__)
app.secret_key = "vinaygautam"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/databasename'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/covid'
db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))



class User(db.Model):
    uid=db.Column(db.Integer,primary_key=True)
    srfid=db.Column(db.String,unique=True)
    email=db.Column(db.String(20))
    dob=db.Column(db.String(20))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/usersignup")
def signup():
    return render_template("usersignup.html")



@app.route("/userlogin")
def login():
    return render_template("userlogin.html")



#testing for database connection
 
@app.route("/test")
def test():
    try:
        #print(f"SQLAlchemy Engine Dialect: {db.get_engine().dialect.name}") # Add this line
        a = Test.query.all()
        print(a)
        return 'MY DATABASE IS CONNECTED'
    except Exception as e:
        print(e)
        return f'MY DATABASE IS NOT CONNECTED {e}'


app.run(debug=True)