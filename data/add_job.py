from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Post', validators=[DataRequired()])
    team_leader = IntegerField('')

    submit = SubmitField('Submit')
