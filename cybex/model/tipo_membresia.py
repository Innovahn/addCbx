# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class tipo_membresia(osv.osv):



    _inherit = 'product.product'

    



    _columns = {


        'membership': fields.boolean('Membership', help='Check if the product is eligible for membership.'),
        'list_price': fields.float(string='cuota en lempiras', help="ingrese el costo de la cuota en lempiras"),
        'tipo':fields.many2one('cybex.categoria','Categoria de membresia',
            help="Elija la categoria a la que pertenece la membresia"),
}
