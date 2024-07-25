from odoo import fields, models


class ResCompanyTypeFields(models.Model):
    _name = "res.company.type.fields"
    _description = "Company Fields"

    name = fields.Char(string="Description", translate=True)
    shortcut = fields.Char(string="Abbreviation", translate=True)
    company_types = fields.Many2many(
        comodel_name="res.partner.company.type", string="Legal Forms"
    )
    field_name = fields.Char()

    _sql_constraints = [
        ("field_name_uniq", "unique (field_name)", "Field Name already exists!")
    ]
