from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class UserForm(FlaskForm):
    id = StringField('id',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired()])
    name = StringField('Name',validators=[DataRequired()])
    service = StringField('Service',validators=[DataRequired()])
    submit = SubmitField('Submit')


class SupplierForm(FlaskForm):
    id = StringField('id',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name',validators=[DataRequired()])
    service = StringField('Service',validators=[DataRequired()])
    submit = SubmitField('Submit')
