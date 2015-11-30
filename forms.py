from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

# from flask_wtf import Form
# from wtforms import StringField, DateField, IntegerField, \
#     SelectField, PasswordField
# from wtforms.validators import DataRequired, Length, EqualTo


class AddNameForm(Form):
    name = StringField('name', validators=[DataRequired()])
