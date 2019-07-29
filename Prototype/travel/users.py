from werkzeug.security import generate_password_hash,check_password_hash
from flask import request,redirect,render_template, url_for, flash
from . import app, l_manager
from flask_login import login_user, logout_user, login_required, current_user
from .models import *
from .forms import *
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out', 'success')
    return render_template('index.html')

@l_manager.user_loader # decorator to return the logged in user
def get_user(user_id):       # this is used by the login manager to retrieve a user, you don't call this function
    u= User.query.filter_by(id=user_id).first()
    return u

@app.route('/register', methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    #this if is true when a form is submitted
    if (register_form.validate_on_submit() == True):
            #get username, password and email from the form
            uname =register_form.user_name.data
            pwd = register_form.password.data
            email=register_form.email_id.data
            # don't store the password - create password hash
            pwd_hash = generate_password_hash(pwd)
            #create a new user model object
            new_user = User(name=uname, password_hash=pwd_hash, emailid=email)
            db.session.add(new_user)
            db.session.commit()
            #commit to the database and redirect to HTML page
            flash('Successfully registered', 'success')
            return redirect(url_for('welcome'))
    #the else is called when there is a get message
    else:
        return render_template('user_forms.html', form=register_form, form_name='Register')



@app.route('/login', methods=['GET', 'POST'])
def authenticate(): #view function
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        #get the username and password from the database
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=user_name).first()
        #if there is no user with that name
        if u1 is None:
            error='Incorrect user name'
        #check the password - notice password hash function
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
            successful='Successfully logged in'
        if error is None:
            #all good, set the login_user
            login_user(u1)
            #this stores from where the user landed at this page
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                flash('Successfully logged in', 'success')
                return redirect(url_for('welcome'))
            return redirect(next)
        else:
            flash(error,'danger')
    #it comes here when it is a get method
    return render_template('user_forms.html', form=login_form, form_name='Login')

@app.route('/management')
@login_required
def personalpc():
#querying the database for all destinations
  print(current_user.id)
  pc = PC.query.filter( PC.user_id == current_user.id)
  xbox = Xbox.query.filter( Xbox.user_id == current_user.id)
  nintendo =  Nintendo.query.filter( Nintendo.user_id == current_user.id)
  playstation = PlayStation.query.filter( PlayStation.user_id == current_user.id)
  #comments = CommentP.query.filter(CommentP.playstation_id == id)
#passing the destinations to template, it shows from database
  return render_template('GameManagement.html', pc=pc,xbox=xbox ,nintendo=nintendo,playstation=playstation)


@app.route('/xbox/update/<id>', methods=['GET', 'POST'])
@login_required
def updateX(id):
  formX = xboxForm()
  xbox1= Xbox.query.filter_by(id=id).first()
  if request.method == 'POST' and formX.validate():
	#creating the destination object and storing in DB
    xbox = Xbox.query.filter_by(id=id).first()
    xbox.name=formX.name.data
    xbox.description=formX.description.data
    xbox.condition=formX.condition.data
    xbox.image=formX.image.data
    xbox.currency=formX.currency.data
    db.session.commit()

    flash('Successfully updated new xbox game', 'success')
    return redirect(url_for('personalpc', id=xbox.id))
  return render_template('xbox_update.html', formX=formX,xbox=xbox1)

@app.route('/pc/update/<id>', methods=['GET', 'POST'])
@login_required
def updateP(id):
  formX = xboxForm()
  Pc1= PC.query.filter_by(id=id).first()
  if request.method == 'POST' and formX.validate():
	#creating the destination object and storing in DB
    Pc = PC.query.filter_by(id=id).first()
    Pc.name=formX.name.data
    Pc.description=formX.description.data
    Pc.condition=formX.condition.data
    Pc.image=formX.image.data
    Pc.currency=formX.currency.data
    db.session.commit()

    flash('Successfully updated new xbox game', 'success')
    return redirect(url_for('personalpc', id=Pc.id))
  return render_template('pc_update.html', formX=formX,xbox=Pc1)


@app.route('/Ps/update/<id>', methods=['GET', 'POST'])
@login_required
def updatePS(id):
  formX = xboxForm()
  PS1= PlayStation.query.filter_by(id=id).first()
  if request.method == 'POST' and formX.validate():
	#creating the destination object and storing in DB
    PS = PlayStation.query.filter_by(id=id).first()
    PS.name=formX.name.data
    PS.description=formX.description.data
    PS.condition=formX.condition.data
    PS.image=formX.image.data
    PS.currency=formX.currency.data
    db.session.commit()

    flash('Successfully updated new xbox game', 'success')
    return redirect(url_for('personalpc', id=PS.id))
  return render_template('playstation_update.html', formX=formX,xbox=PS1)

@app.route('/nin/update/<id>', methods=['GET', 'POST'])
@login_required
def updateN(id):
  formX = xboxForm()
  nin1= Nintendo.query.filter_by(id=id).first()
  if request.method == 'POST' and formX.validate():
	#creating the destination object and storing in DB
    nin = Nintendo.query.filter_by(id=id).first()
    nin.name=formX.name.data
    nin.description=formX.description.data
    nin.condition=formX.condition.data
    nin.image=formX.image.data
    nin.currency=formX.currency.data
    db.session.commit()

    flash('Successfully updated new xbox game', 'success')
    return redirect(url_for('personalpc', id=nin.id))
  return render_template('nintendo_update.html', formX=formX,xbox=nin1)


@app.route('/orders')
@login_required
def personalorders():
#querying the database for all destinations
  pcOder = OrderPC.query.filter( OrderPC.buyer_id == current_user.id)
  xboxOder = OrderX.query.filter( OrderX.buyer_id == current_user.id)
  nintendoOder =  OrderNi.query.filter( OrderNi.buyer_id == current_user.id)
  playstationOder = OrderPS.query.filter( OrderPS.buyer_id == current_user.id)
  #comments = CommentP.query.filter(CommentP.playstation_id == id)
#passing the destinations to template, it shows from database
  return render_template('Bookings.html', pcOder=pcOder,xboxOder=xboxOder ,nintendoOder=nintendoOder,playstationOder=playstationOder)