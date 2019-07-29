from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo


class pcForm(FlaskForm):
  name = StringField('Game name', validators=[DataRequired()])
  description = TextAreaField('Description', validators=[DataRequired()])
  image = StringField('Game image coever', validators=[DataRequired()])
  currency = StringField('Game price', validators=[DataRequired()])
  condition = SelectField(u'Condition', choices=[('Brand New', 'Brand New'), ('Second-Hand', 'Second-Hand'), ('Booked','Booked')])
  submit = SubmitField("Create")


class xboxForm(FlaskForm):
  name = StringField('Game name', validators=[DataRequired()])
  description = TextAreaField('Description', validators=[DataRequired()])
  image = StringField('Game image coever', validators=[DataRequired()])
  currency = StringField('Game price', validators=[DataRequired()])
  condition = SelectField(u'Condition', choices=[('Brand New', 'Brand New'), ('Second-Hand', 'Second-Hand'), ('Booked','Booked')])
  submit = SubmitField("Create")

class nintendoForm(FlaskForm):
  name = StringField('Game name', validators=[DataRequired()])
  description = TextAreaField('Description', validators=[DataRequired()])
  image = StringField('Game image coever', validators=[DataRequired()])
  currency = StringField('Game price', validators=[DataRequired()])
  condition = SelectField(u'Condition', choices=[('Brand New', 'Brand New'), ('Second-Hand', 'Second-Hand'), ('Booked','Booked')])
  submit = SubmitField("Create")

class playstationForm(FlaskForm):
  name = StringField('Game name', validators=[DataRequired()])
  description = TextAreaField('Description', validators=[DataRequired()])
  image = StringField('Game image coever', validators=[DataRequired()])
  currency = StringField('Game price', validators=[DataRequired()])
  condition = SelectField(u'Condition', choices=[('Brand New', 'Brand New'), ('Second-Hand', 'Second-Hand'), ('Booked','Booked')])
  submit = SubmitField("Create")

class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [DataRequired()])
  submit = SubmitField("Create")

class RegisterForm(FlaskForm):
  user_name = StringField("User Name", validators=[InputRequired()])
  email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
  password = PasswordField("Password",
                           validators=[InputRequired(), EqualTo('confirm', message="Passwords should match")])
  confirm = PasswordField("Confirm Password")
  submit = SubmitField("Register")

class LoginForm(FlaskForm):
  user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
  password = PasswordField("Password", validators=[InputRequired('Enter user password')])
  submit = SubmitField("Login")

class BookForm(FlaskForm):
  date = DateField("Booking Date", validators=[InputRequired('Enter date')])
  submit = SubmitField("Book")