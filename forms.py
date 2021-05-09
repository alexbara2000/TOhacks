from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField(
        'Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            DataRequired()
        ]
    )
    body = SelectField('Province', choices=['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia', 'Ontario', 'Prince Edward Island', 'Quebec', 'Saskatchewan'])
    submit = SubmitField('Submit')
