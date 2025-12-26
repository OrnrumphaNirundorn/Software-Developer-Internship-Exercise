from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'

    # 1. Title (required)
    name = fields.Char(
        string='Todo Title',
        required=True
    )

    # 2. Tags
    tag_ids = fields.Many2many(
        'todo.tag',
        string='Tags'
    )

    # 3. Dates (required)
    start_date = fields.Date(
        string='Start Date',
        required=True
    )

    end_date = fields.Date(
        string='End Date',
        required=True
    )

    # 4. Status tracking
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('in_progress', 'In Progress'),
            ('done', 'Complete'),
        ],
        string='Status',
        default='draft',
        tracking=True
    )

    # 5. Date validation
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date:
                if record.end_date < record.start_date:
                    raise ValidationError(
                        'End Date must be later than Start Date.'
                    )

    # 6. Button actions
    def action_start(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'in_progress'

    def action_done(self):
        for record in self:
            if record.state == 'in_progress':
                record.state = 'done'
