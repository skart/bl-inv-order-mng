
from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms_components import read_only

class InvForm(FlaskForm):
    part_num = StringField('Part Number', validators=[DataRequired()])
    part_type = SelectField('Type', choices = [('PART', 'Part')])
    color_name = SelectField('Color', coerce=int, validators = [DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    new_or_used = SelectField('New or Used', choices = [('N', 'New'), ('U', 'Used')]  , validators = [DataRequired()])
    unit_price = StringField('Price', validators=[DataRequired()])
    description = TextAreaField('Description')
    remarks = StringField('Drawer', validators=[DataRequired()])
    is_stock_room = BooleanField('Stockroom?')
    submit = SubmitField('Submit') 

    def __init__(self, *args, **kwargs):
        super(InvForm, self).__init__(*args, **kwargs)
        read_only(self.part_type)
        read_only(self.color_name)
        read_only(self.new_or_used)