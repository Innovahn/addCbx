# -*- coding: utf-8 -*-
{	
	'name' : 'cybex',
	'author': 'Grupo Innova',
	'category': 'Membresias',
	'summary': 'Membresias',
	'description': """
Socios,Membresias,Tipos de Membrecias
==================================
Con este módulo, OpenERP  y Grupo Innova le ayudan a la gestión de todas sus membresias, la administracion
de cada uno de sus clientes asociados y poseedores de una membresia. el modulo membresias le ayuda en la
creacion de nuevos contratos donde se manejara toda la informacion necesaria para la inscripcion de un nuevo
socio, tambien maneja lo que son demoras en los contratos y los socios que no estan activos mediante fechas
de vencimiento.


Características principales
-------------
* Creacion de nuevos socios
* Creacion de Contratos
* Recordatorio cuando un contrato llegue a su fecha de caducidad
* Nuevos tipos de membrecias
* Mostrar los clientes morosos hasta la fecha actual
* Gráficos de ventas y membresias
""",
	'data':[
	    'security/ir.model.access.csv',
	    'views/tipo_membresia_view.xml',
             'views/partner_view.xml',
             'views/categoria_view.xml',
	     'views/socio_data.xml',
	     'views/factura_view.xml',
	     'views/pedidoventa_view.xml',
	     
	    ],
	'depends': ['base','product','sale','account_voucher'],
	'installable': True,
	'init_xml': [],
    	'update_xml': [
    ],
    'installable': True,
    'active': False,

}
