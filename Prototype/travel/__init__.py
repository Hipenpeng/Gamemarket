from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
#this is the main package file where flask is instantiated

app = Flask(__name__, instance_relative_config=True)
app.debug=True
app.secret_key="SecretKey"
Bootstrap(app)


db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///travel.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


l_manager = LoginManager()
l_manager.init_app(app)
l_manager.login_view='/login'

# landing page route
@app.route('/')
def welcome():
    return render_template('index.html')

#to avoid use of blueprints, we declare all routes in destination file
# import it at the end - to ensure all the routes declared in this module are available
import travel.games
import travel.users