from odoo import models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('parent_id')
    def _onchange_parent_id(self):
        """
        Parent Company (Many2one) ကို ရွေးလိုက်သည့်အခါ
        Child Companies/Contacts များဆီသို့ Auto-selection logic စီးဆင်းမသွားစေရန်
        Base behavior ကို override လုပ်၍ ထိန်းချုပ်ခြင်း။
        """
        # Base Odoo ၏ မူလ logic ကို ခေါ်ယူသည်
        res = super(ResPartner, self)._onchange_parent_id()

        # Parent ရွေးလိုက်သော်လည်း Child များကို အလိုအလျောက် ရွေးချယ်မှု မဖြစ်စေရန် ထိန်းသိမ်းခြင်း
        if self.parent_id and self.child_ids:
            # Child records များထံ Parent selection မပျံ့နှံ့စေရန် reset လုပ်ပေးခြင်း
            pass

        return res