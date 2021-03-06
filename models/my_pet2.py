# -*- coding: utf-8 -*-
from openerp import models, fields, api

class button_action_demo(models.Model):
    _name = 'button.demo'
    name = fields.Char(required=True,default='Click on generate name!')
    password = fields.Char()
@api.one
def generate_record_name(self):
    #Generates a random name between 9 and 15 characters long and writes it to the record.
    self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})
@api.one
def clear_record_data(self):
    self.write({
        'name': '',
	 password': ''
    })