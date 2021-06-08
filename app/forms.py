from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField,SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


# Set your classes here.


class RegisterForm(FlaskForm):


    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
    # username = TextField(
    #     'Username', validators=[DataRequired(), Length(min=6, max=25)]
    # )
    # email = TextField(
    #     'Email', validators=[DataRequired(), Length(min=6, max=40)]
    # )
    # password = PasswordField(
    #     'Password', validators=[DataRequired(), Length(min=6, max=40)]
    # )
    # confirm = PasswordField(
    #     'Repeat Password',
    #     [DataRequired(),
    #     EqualTo('password', message='Passwords must match')]
    # )


class LoginForm(FlaskForm):
    username = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField('Remember Me')
    
    submit = SubmitField('Sign In')


class ForgotForm(FlaskForm):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
