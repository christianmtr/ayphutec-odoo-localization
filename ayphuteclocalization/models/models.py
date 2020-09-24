# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reportfourtenone(models.Model):
    _name = 'ayphuteclocalization.reportfourtenone'
    _description = 'Reporte 14.01'

    journal_sub_type = fields.Char(default='05', string="NUMERO CORRELATIVO DEL REGISTRO CODIGO UNICO DE LA OPERACION", compute='_get_values')
    sequence = fields.Char(compute='_get_values')
    invoice_date = fields.Date(string='Invoice Date', compute='_get_values')
    invoice_date_due = fields.Date(string='Due Date', compute='_get_values')
    document_type = fields.Char(default='01', compute='_get_values')
    journal_code = fields.Char(string='Short Code', size=5, required=True, compute='_get_values')
    journal_sequence_number_next = fields.Integer(string='Next Number', compute='_get_values')
    identitication_type = fields.Char(compute='_get_values')
    partner_vat = fields.Char(string='Identification Number', compute='_get_values')
    partner_name = fields.Char(compute='_get_values')
    export_invoice_value = fields.Char(default='', compute='_get_values')
    move_amount_untaxed = fields.Char(compute='_get_values')
    exonerated = fields.Char(default='0.00', compute='_get_values')
    unaffected = fields.Char(default='0.00', compute='_get_values')
    isc = fields.Char(default='0.00', compute='_get_values')
    igv = fields.Char(compute='_get_values')
    plastic_bag_tax = fields.Char(default='0.00', compute='_get_values')
    others = fields.Char(default='0.00', compute='_get_values')
    move_amount_total = fields.Char(compute='_get_values')
    exchange_rate = fields.Char(default='', compute='_get_values')
    original_document_date = fields.Char(default='//', compute='_get_values')
    original_document_type = fields.Char(default='', compute='_get_values')
    original_document_sequence = fields.Char(default='', compute='_get_values')
    original_document_number = fields.Char(default='', compute='_get_values')

    @api.depends('account.move.invoice_date', 'account.move.invoice_date_due', 'account.journal.code', 'account.journal.sequence_number_next', 'res.partner.l10_latam_identification_type_id', 'res.partner.vat', 'res.partner.name', 'account.move.amount_untaxed', 'account.move.amount_by_group', 'account.move.amount_total')
    def _get_values(self):
        for record in self:
            record.journal_sub_type = '05'
            record.sequence = '0001'
            record.invoice_date = record.account.move.invoice_date
            record.invoice_date_due = record.account.move.invoice_date_due
            record.document_type = ''
            record.journal_code = record.account.journal_code
            record.journal_sequence_number_next = record.account.journal.sequence_number_next
            record.identitication_type = record.res.partner.l10_latam_identification_type_id
            record.partner_vat = record.res.partner.vat
            record.partner_name = record.res.partner.name
            record.export_invoice_value = ''
            record.move_amount_untaxed = record.account.move.amount_untaxed
            record.exonerated = '0.00'
            record.unaffected = '0.00'
            record.isc = '0.00'
            record.igv = record.account.move.amount_by_group
            record.plastic_bag_tax = '0.00'
            record.others = '0.00'
            record.move_amount_total = record.account.move.amount_total
            record.exchange_rate = ''
            record.original_document_date = '//'
            record.original_document_type = ''
            record.original_document_sequence = ''
            record.original_document_number = ''
