from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length

class subForm(FlaskForm):
    topic = StringField(u"topic",validators=[Length(1, 64)])
    submit = SubmitField(u'OK')
    