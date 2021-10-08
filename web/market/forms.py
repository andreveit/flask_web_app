from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    
    def validate_username(FlaskForm, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError('This username already exists, please try a different one.')

    def validate_email_address(FlaskForm, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators= [Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators= [Length(min=3), DataRequired()])
    password2 = PasswordField(label='Password confirmation', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Submit')


class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Buy')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell')
