from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,  ValidationError
from model import Supplier, User

class UserForm(FlaskForm):
    id = StringField('id',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    firstName = StringField('firstName',validators=[DataRequired()])
    lastName = StringField('lastName',validators=[DataRequired()])
    address = StringField('address',validators=[DataRequired()])
    city = StringField('city',validators=[DataRequired()])
    phoneNumber = StringField('phoneNumber',validators=[DataRequired()])
    service = StringField('Service',validators=[DataRequired()])
    note = StringField('Service',validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_username(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please use a different name.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class SupplierForm(FlaskForm):
    id = StringField('id',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    firstName = StringField('firstName',validators=[DataRequired()])
    lastName = StringField('lastName',validators=[DataRequired()])
    address = StringField('address',validators=[DataRequired()])
    phoneNumber = StringField('phoneNumber',validators=[DataRequired()])
    service = StringField('Service',validators=[DataRequired()])
    note = StringField('Service',validators=[DataRequired()])

    submit = SubmitField('Submit')

    def validate_username(self, name):
        user = Supplier.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please use a different name.')

    def validate_email(self, email):
        user = Supplier.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
