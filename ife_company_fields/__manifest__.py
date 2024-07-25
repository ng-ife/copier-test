# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Add Company Fields",
    "summary": "Adds field names to Company based on their company type",
    "version": "16.0.1.0.2",
    "license": "LGPL-3",
    "author": "IFE Gesellschaft für Forschung und Entwicklung",
    "website": "https://www.ife.de",
    "depends": ["partner_company_type"],
    "data": [
        "security/res_company_type_fields.xml",
        "views/res_company_type_fields.xml",
    ],
    "auto_install": True,
    "installable": True,
}
