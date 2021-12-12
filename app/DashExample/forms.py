from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange, ValidationError

# login and registration


class AddDataForm(FlaskForm):
    temperature = IntegerField('Temperature', id='temperature', validators=[
        InputRequired(), NumberRange(min=0, max=50, message='Temperature must be between 0 to 50')
    ])
    ph = IntegerField('pH', id='ph', validators=[
        InputRequired(), NumberRange(min=0, max=14, message='Temperature must be between 0 to 50')
    ])
    ec = IntegerField('EC', id='ec', validators=[
        InputRequired(), NumberRange(min=0, max=4000, message='Temperature must be between 0 to 50')
                                                 ])
    orp = IntegerField('ORP', id='orp', validators=[
        InputRequired(), NumberRange(min=0, max=400, message='Temperature must be between 0 to 50')
                                                    ])
    ammonia = IntegerField('Ammonia', id='ammonia', validators=[
        InputRequired(), NumberRange(min=0, max=2000, message='Temperature must be between 0 to 50')
                                                                ])
    nitrite = IntegerField('Nitrite', id='nitrite', validators=[
        InputRequired(), NumberRange(min=0, max=50, message='Temperature must be between 0 to 50')
                                                                ])
    nitrate = IntegerField('Nitrate', id='nitrate', validators=[
        InputRequired(), NumberRange(min=0, max=50, message='Temperature must be between 0 to 50')
                                                                ])
    oxygen = IntegerField('Oxygen', id='oxygen', validators=[
        InputRequired(), NumberRange(min=0, max=100, message='Temperature must be between 0 to 50')
    ])
