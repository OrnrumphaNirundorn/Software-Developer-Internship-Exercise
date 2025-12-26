from odoo import models, fields


class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tag'

    name = fields.Char(
        string='Tag Name',
        required=True
    )
