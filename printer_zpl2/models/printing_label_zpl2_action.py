# Copyright 2021 Studio73 - Iván Pérez <ivan.perez@studio73.es>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class PrintingLabelZpl2Action(models.Model):
    _name = "printing.label.zpl2.action"
    _description = "Printing Label Zpl2 Action"

    label_id = fields.Many2one(
        comodel_name="printing.label.zpl2",
        string="Label",
        required=True,
        ondelete="cascade",
    )
    user_id = fields.Many2one(
        comodel_name="res.users", string="Usuario", required=True, ondelete="cascade"
    )
    printer_id = fields.Many2one(comodel_name="printing.printer", string="Impresora")
