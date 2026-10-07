/** @odoo-module **/

import { SwitchCompanyMenu } from "@web/webclient/switch_company_menu/switch_company_menu";
import { patch } from "@web/core/utils/patch";

patch(SwitchCompanyMenu.prototype, {
    setup() {
        super.setup();
    },

    // Selected Companies များထဲမှ နှိပ်လိုက်သော ကုမ္ပဏီတစ်ခုတည်းကိုသာ Activate လုပ်ရန်
    toggleCompany(isAllowed, companyId) {
        const selectedId = Array.isArray(companyId) ? companyId[0] : companyId;
        this.companyService.setCompanies("replace", selectedId);
    }
});