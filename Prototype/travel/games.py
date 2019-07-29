from . import app
from flask import render_template, request, flash, redirect, url_for
from datetime import datetime
from travel import db
from flask_login import login_required, current_user
from .models import *
from .forms import *

comments= list()

#print(comments)
@app.route('/pc_games')
def pc():
#querying the database for all destinations
  pc = PC.query.all()
#passing the destinations to template, it shows from database
  return render_template('pc_games.html', pc=pc)

@app.route('/xbox_games')
def xbox():
#querying the database for all destinations
  xbox = Xbox.query.all()

#passing the destinations to template, it shows from database
  return render_template('xbox_games.html', xbox=xbox)

@app.route('/nintendo_games')
def nintendo():
#querying the database for all destinations
  nintendo = Nintendo.query.all()
#passing the destinations to template, it shows from database
  return render_template('nintendo_games.html', nintendo=nintendo)

@app.route('/playstation_games')
def playstation():
#querying the database for all destinations
  playstation = PlayStation.query.all()
#passing the destinations to template, it shows from database
  return render_template('playstation_games.html', playstation=playstation)


@app.route('/game/create/xbox', methods = ['GET', 'POST'])
@login_required
def createX():
  formX = xboxForm()
  if request.method == 'POST' and formX.validate():
	#creating the destination object and storing in DB
    xbox = Xbox(name=formX.name.data,
                description=formX.description.data,
                image=formX.image.data,
                currency=formX.currency.data,
                user_id=current_user.id,
                user_name=current_user.name,
                user_email=current_user.emailid,
                condition=formX.condition.data
                )
    db.session.add(xbox)
    db.session.commit()

    flash('Successfully created new xbox game', 'success')
    return redirect(url_for('showX', id=xbox.id))
  return render_template('xbox_create.html', formX=formX)


@app.route('/game/create/pc', methods = ['GET', 'POST'])
@login_required
def create():
  form = pcForm()
  if request.method == 'POST' and form.validate():
	#creating the destination object and storing in DB
    pc = PC(name=form.name.data,
                description=form.description.data,
                image=form.image.data,
                currency=form.currency.data,
                user_id=current_user.id,
                user_name=current_user.name,
                user_email=current_user.emailid,
                condition=form.condition.data)
    db.session.add(pc)
    db.session.commit()

    flash('Successfully created new pc game', 'success')
    return redirect(url_for('show', id=pc.id))
  return render_template('pc_create.html', form=form)

@app.route('/game/create/playstation', methods = ['GET', 'POST'])
@login_required
def createP():
  formP = playstationForm()
  if request.method == 'POST' and formP.validate():
	#creating the destination object and storing in DB
    playstation = PlayStation(name=formP.name.data,
                description=formP.description.data,
                image=formP.image.data,
                currency=formP.currency.data,
                user_id=current_user.id,
                user_name=current_user.name,
                user_email=current_user.emailid,
                condition=formP.condition.data)
    db.session.add(playstation)
    db.session.commit()

    flash('Successfully created new playstation game', 'success')
    return redirect(url_for('showP', id=playstation.id))
  return render_template('playstation_create.html', formP=formP)


@app.route('/game/create/nintendo', methods = ['GET', 'POST'])
@login_required
def createN():
  formN = nintendoForm()
  if request.method == 'POST' and formN.validate():
	#creating the destination object and storing in DB
    nintendo = Nintendo(name=formN.name.data,
                description=formN.description.data,
                image=formN.image.data,
                currency=formN.currency.data,
                user_id=current_user.id,
                user_name=current_user.name,
                user_email=current_user.emailid,
                condition=formN.condition.data)
    db.session.add(nintendo)
    db.session.commit()

    flash('Successfully created new nintendo game', 'success')
    return redirect(url_for('showN', id=nintendo.id))
  return render_template('nintendo_create.html', formN=formN)

@app.route('/nintendoGames/<id>',methods = ['GET', 'POST'])
@login_required
def showN(id):

    bookform = BookForm()
    form = CommentForm()
    nintendo = Nintendo.query.filter_by(id=id).first()
    comments = Comment.query.filter(Comment.nintendo_id == id)
    if request.method == 'POST' and bookform.validate():
        # creating the destination object and storing in DB
        past = datetime.strptime(str(bookform.date.data), "%Y-%m-%d")
        present = datetime.now()

        if past.date() < present.date():
            flash("Sorry, you must pick a date greater than today", 'danger')
        elif nintendo.condition == 'booked':
            flash('Sorry, it has been booked', 'danger')
        else:
            order = OrderNi()
            order.date = bookform.date.data
            order.buyer_id = current_user.id
            order.owner_id = nintendo.user_id
            order.nintendo_id= nintendo.id
            order.owner_name = nintendo.user_name
            order.image = nintendo.image
            nintendo.condition = 'booked'
            db.session.add(order)
            db.session.commit()
            flash('Successfully booked new PC game', 'success')
    return render_template('nintendo_show.html', nintendo=nintendo, form=form, comments=comments, bookform=bookform)

@app.route('/playstationGames/<id>',methods = ['GET', 'POST'])
@login_required
def showP(id):
    bookform = BookForm()
    form = CommentForm()
    playstation = PlayStation.query.filter_by(id=id).first()
    comments = CommentP.query.filter(CommentP.playstation_id == id)
    if request.method == 'POST' and bookform.validate():
        # creating the destination object and storing in DB
        past = datetime.strptime(str(bookform.date.data), "%Y-%m-%d")
        present = datetime.now()

        if past.date() < present.date():
            flash("Sorry, you must pick a date greater than today", 'danger')
        elif nintendo.condition == 'booked':
            flash('Sorry, it has been booked', 'danger')
        else:
            order = OrderPS()
            order.date = bookform.date.data
            order.buyer_id = current_user.id
            order.owner_id = playstation.user_id
            order.playstation_id = playstation.id
            order.owner_name = playstation.user_name
            order.image = playstation.image
            playstation.condition = 'booked'
            db.session.add(order)
            db.session.commit()
            flash('Successfully booked new PC game', 'success')
    return render_template('playstation_show.html', playstation=playstation, form=form, comments=comments, bookform=bookform)

@app.route('/xboxGames/<id>',methods = ['GET', 'POST'])
@login_required
def showX(id):
    bookform = BookForm()
    form = CommentForm()
    xbox = Xbox.query.filter_by(id=id).first()
    comments = CommentX.query.filter(CommentX.xbox_id == id)
    if request.method == 'POST' and bookform.validate():
        # creating the destination object and storing in DB
        past = datetime.strptime(str(bookform.date.data), "%Y-%m-%d")
        present = datetime.now()

        if past.date() < present.date():
            flash("Sorry, you must pick a date greater than today", 'danger')
        elif nintendo.condition == 'booked':
            flash('Sorry, it has been booked', 'danger')
        else:
            order = OrderX()
            order.date = bookform.date.data
            order.buyer_id = current_user.id
            order.owner_id = xbox.user_id
            order.xbox_id = xbox.id
            order.owner_name = xbox.user_name
            order.image = xbox.image
            xbox.condition = 'booked'
            db.session.add(order)
            db.session.commit()
            flash('Successfully booked new xbox game', 'success')


    return render_template('xbox_show.html', xbox=xbox, form=form, comments=comments, bookform=bookform)

@app.route('/pcGames/<id>', methods = ['GET', 'POST'])
@login_required
def show(id):
    bookform =BookForm()
    form = CommentForm()
    pc = PC.query.filter_by(id=id).first()
    comments = CommentPC.query.filter(CommentPC.pc_id == id)
    if request.method == 'POST' and bookform.validate():
        past = datetime.strptime(str(bookform.date.data), "%Y-%m-%d")
        present = datetime.now()

        if past.date() < present.date():
            flash("Sorry, you must pick a date greater than today", 'danger')
        elif nintendo.condition == 'booked':
            flash('Sorry, it has been booked', 'danger')
        else:
            order = OrderPC()
            order.date = bookform.date.data
            order.buyer_id = current_user.id
            order.owner_id = pc.user_id
            order.pc_id = pc.id
            order.owner_name = pc.user_name
            order.image = pc.image
            xbox.condition = 'booked'
            db.session.add(order)
            db.session.commit()
            flash('Successfully booked new xbox game', 'success')

    return render_template('pc_show.html', pc=pc, form=form, comments=comments, bookform=bookform)

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def forbidden(e):
    return render_template('500.html'), 500

@app.route('/nintendo/<nintendo>/comment', methods = ['GET', 'POST'])
@login_required
def comment(nintendo):
    form = CommentForm()
    nintendo = Nintendo.query.filter_by(id=nintendo).first()
    if request.method == 'POST' and form.validate():
        comment = Comment(text=form.text.data, user_id=current_user.id, nintendo_id=nintendo.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added. ' + form.text.data, 'success')
        return redirect(url_for('showN', id=nintendo.id))

@app.route('/playstation/<playstation>/comment', methods = ['GET', 'POST'])
@login_required
def commentP(playstation):
    form = CommentForm()
    playstation = PlayStation.query.filter_by(id=playstation).first()
    if request.method == 'POST' and form.validate():
        comment = CommentP(text=form.text.data, user_id=current_user.id, playstation_id=playstation.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added. ' + form.text.data, 'success')
        return redirect(url_for('showP', id=playstation.id))

@app.route('/xbox/<xbox>/comment', methods = ['GET', 'POST'])
@login_required
def commentX(xbox):
    form = CommentForm()
    xbox = Xbox.query.filter_by(id=xbox).first()
    if request.method == 'POST' and form.validate():
        comment = CommentX(text=form.text.data, user_id=current_user.id, xbox_id=xbox.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added. ' + form.text.data, 'success')
        return redirect(url_for('showX', id=xbox.id))

@app.route('/pc/<pc>/comment', methods = ['GET', 'POST'])
@login_required
def commentPC(pc):
    form = CommentForm()
    pc = PC.query.filter_by(id=pc).first()
    if request.method == 'POST' and form.validate():
        comment = CommentPC(text=form.text.data, user_id=current_user.id, pc_id=pc.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added. ' + form.text.data, 'success')
        return redirect(url_for('show', id=pc.id))

