from odoo import models, fields

class MyAppModel(models.Model):
    _name = 'my.app.model'
    _description = 'My App Model'
    # mail.thread နှင့် mail.activity.mixin မဖြစ်မနေ ပါရပါမည်
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', required=True, tracking=True)

    # 2. Status ပြောင်းလဲပေးမည့် Button Action များ
    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'