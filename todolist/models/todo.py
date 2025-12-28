from odoo import _, api, fields, models
from odoo.exceptions import ValidationError, UserError

class TodoList(models.Model):
    _name = 'todolist'
    _description = 'TodoList'

    name = fields.Char('Title', required=True)
    tags_ids = fields.Many2many('todotags', string='Tags')
    
    start_date_time = fields.Datetime('Start Date', required=True)
    end_date_time = fields.Datetime('End Date', required=True)

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('in_progress', 'In Progress'),
            ('done', 'Complete'),
        ],
        string='Status', default='draft'
    )

    def action_progress(self):
        for record in self:
            record.state = 'in_progress'



    @api.constrains('start_date_time', 'end_date_time')
    def _constrains_DateChecker(self):
        for record in self:
            if record.start_date_time and record.end_date_time:
                if record.start_date_time > record.end_date_time:
                    raise ValidationError('Start date and time more than end date and time')


class TodoTags(models.Model):
    _name = 'todotags'
    _description = 'TodoTags'

    name = fields.Char('name')
