# -*- coding: utf-8 -*-

from odoo import models, fields, api


class report_fourten_one(models.Model):
    _name = 'ayphutec-localization.report_fourten_one'
    _description = 'Reporte 14.01'

    journal_sub_type = fields.Char(default='05')
    sequence = fields.Char()
    invoice_date = fields.Date(string='Invoice/Bill Date')
    invoice_date_due = fields.Date(string='Due Date')
    document_type = fields.Char(default='01')
    journal_code = fields.Char()
    journal_sequence_number_next = fields.Char()
    identitication_type = fields.Char()
    partner_vat = fields.Char()
    partner_name = fields.Char()
    export_invoice_value = fields.Char(default='')
    move_amount_untaxed = fields.Char()
    exonerated = fields.Char(default='0.00')
    unaffected = fields.Char(default='0.00')
    isc = fields.Char(default='0.00')
    igv = fields.Char()
    plastic_bag_tax = fields.Char(default='0.00')
    others = fields.Char(default='0.00')
    move_amount_total = fields.Char()
    exchange_rate = fields.Char(default='')
    original_document_date = fields.Char('//')
    original_document_type = fields.Char('')
    original_document_sequence = fields.Char('')
    original_document_number = fields.Char('')

    @api.depends('account.move.invoice_date', 'account.move.invoice_date_due', 'account.journal.code', 'account.journal.sequence_number_next', 'res.partner.l10_latam_identification_type_id', 'res.partner.vat', 'res.partner.name', 'account.move.amount_untaxed', 'account.move.amount_by_group', 'account.move.amount_total')
    def _get_values(self):
        for record in self:
            record.invoice_date = record.account.move.invoice_date
            record.invoice_date_due = record.account.move.invoice_date_due
            record.journal_code = record.account.journal_code
            record.journal_sequence_number_next = record.account.journal.sequence_number_next
            record.identitication_type = record.res.partner.l10_latam_identification_type_id
            record.partner_vat = record.res.partner_vat
            record.partner_name = record.res.partner_name
            record.move_amount_untaxed = record.account.move.amount_untaxed
            record.igv = record.account.move.amount_by_group
            record.move_amount_total = record.account.move.amount_total
