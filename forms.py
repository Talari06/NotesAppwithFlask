from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class NoteForm(FlaskForm):
    note = TextAreaField('Note', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Add Note')

class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')
