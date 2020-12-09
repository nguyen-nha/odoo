# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "my.pet"
    _inherit = 'sale.order'
    _description = "My pet model"

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    petname = fields.Char('Petname')
    description = fields.Text('Pet Description')
    lastname = fields.Char('lastname')
    age = fields.Integer('Pet Age', default=1)
    name_t = fields.Char('namet', default=True)
    select = fields.Selection([
        ('true', 'false'),
        ('false', 'true')
    ], string='select', default='true')
    weight = fields.Float('Weight (kg)')
    dob = fields.Date('DOB', required=False)
    baden = fields.Char('Ba Den', default='true')
    consignment = fields.Boolean('Ky Gui',default=False)
    lastname = fields.Char('lastname')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")
    owner_ids = fields.Many2many('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                string="Related Products",
                                relation='pet_product_rel',
                                column1='col_pet_id',
                                column2='col_product_id')

    pet_line = fields.One2many('my.pet.line', 'pet_id', string='Order Lines', )

class MyPetline(models.Model):
    _name = "my.pet.line"
    _description = "My pet model"
    pet_id = fields.Many2one('my.pet')
    petname = fields.Char(string='Petname')
    nickname = fields.Integer(string='Nickname')
    petname = fields.Char(string='Pet Age')
    weight = fields.Integer(sting='Weight')
    DOB = fields.Char(string='DOB')

class ResPartners(models.Model):
        _name = 'res.partners'
        _description = 'Partners'
        _rec_name = 'display_name'
        display_name = fields.Char(string='Name', required=True)
        email = fields.Char('Email', required=True)
        mobile = fields.Char('Mobile', required=True)

















