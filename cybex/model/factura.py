# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from datetime import datetime
class factura(osv.Model):



	_inherit = 'account.invoice'

	




	_columns = {
        		
		'nombre_cliente':fields.char('Factura a Nombre de:',type="char",help="Ingrese el nombre del cliente que aparecera en la factura"),

		'linea_pedido':fields.integer('Referencia de linea'),
            }
	
     
       

