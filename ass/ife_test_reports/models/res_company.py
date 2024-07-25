from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    has_company_fields = fields.Boolean(compute="_compute_company_fields")

    partner_company_type = fields.Many2one(related="partner_id.partner_company_type_id")
    company_fields = fields.Many2many(comodel_name="res.company.type.fields")
    registry_court = fields.Char()
    managing_directors = fields.Many2many(comodel_name="res.partner", relation="managing_directors_rel")
    board_chair = fields.Many2many(
        comodel_name="res.partner", relation="board_chair_rel", string="Chairmen of the Board"
    )
    board_of_directors = fields.Many2many(
        comodel_name="res.partner", relation="board_of_direcotrs_rel", string="Board of Directors"
    )
    supervisory_board_chair = fields.Many2many(
        comodel_name="res.partner", relation="supervisory_board_rel", string="Chairmen of the Supervisory Board"
    )
    personal_liable_partner = fields.Many2one(comodel_name="res.partner")

    has_registry_court = fields.Boolean(compute="_compute_company_fields", default="False")
    has_managing_directors = fields.Boolean(compute="_compute_company_fields", default="False")
    has_board_chair = fields.Boolean(compute="_compute_company_fields", default="False")
    has_board_of_directors = fields.Boolean(compute="_compute_company_fields", default="False")
    has_supervisory_board_chair = fields.Boolean(compute="_compute_company_fields", default="False")
    has_personal_liable_partner = fields.Boolean(compute="_compute_company_fields", default="False")

    abr_registry_court = fields.Char(compute="_compute_company_fields")
    abr_managing_directors = fields.Char(compute="_compute_company_fields")
    abr_board_chair = fields.Char(compute="_compute_company_fields")
    abr_board_of_directors = fields.Char(compute="_compute_company_fields")
    abr_supervisory_board_chair = fields.Char(compute="_compute_company_fields")
    abr_personal_liable_partner = fields.Char(compute="_compute_company_fields")

    def _compute_company_fields(self):
        for record in self:
            record["has_company_fields"] = False
            for field in record.env["res.company.type.fields"].search([]):
                field_key = "has_{}".format(field.field_name)
                field_key_abr = "abr_{}".format(field.field_name)
                if record.partner_company_type in field.company_types:
                    record["has_company_fields"] = True
                    record[field_key] = True
                    record[field_key_abr] = field.shortcut
                else:
                    record[field_key] = False
                    record[field_key_abr] = ""


class BaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"

    has_company_fields = fields.Boolean(related="company_id.has_company_fields")

    registry_court = fields.Char(related="company_id.registry_court")
    managing_directors = fields.Many2many(related="company_id.managing_directors")
    board_chair = fields.Many2many(related="company_id.board_chair")
    board_of_directors = fields.Many2many(related="company_id.board_of_directors")
    supervisory_board_chair = fields.Many2many(related="company_id.supervisory_board_chair")
    personal_liable_partner = fields.Many2one(related="company_id.personal_liable_partner")

    has_registry_court = fields.Boolean(related="company_id.has_registry_court")
    has_managing_directors = fields.Boolean(related="company_id.has_managing_directors")
    has_board_chair = fields.Boolean(related="company_id.has_board_chair")
    has_board_of_directors = fields.Boolean(related="company_id.has_board_of_directors")
    has_supervisory_board_chair = fields.Boolean(related="company_id.has_supervisory_board_chair")
    has_personal_liable_partner = fields.Boolean(related="company_id.has_personal_liable_partner")

    abr_registry_court = fields.Char(related="company_id.abr_registry_court")
    abr_managing_directors = fields.Char(related="company_id.abr_managing_directors")
    abr_board_chair = fields.Char(related="company_id.abr_board_chair")
    abr_board_of_directors = fields.Char(related="company_id.abr_board_of_directors")
    abr_supervisory_board_chair = fields.Char(related="company_id.abr_supervisory_board_chair")
    abr_personal_liable_partner = fields.Char(related="company_id.abr_personal_liable_partner")
