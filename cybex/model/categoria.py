# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class categoria(osv.Model):

	_name = 'cybex.categoria'
	_columns = {
	   'name': fields.text('Categoria', help="Ingrese un nombre para la categoria"),
            'codigo': fields.text('Codigo de categoria', help="Ingrese el codigo de la categoria"),
}