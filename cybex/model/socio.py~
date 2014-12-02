# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from datetime import datetime
class partner(osv.Model):



	_inherit = 'res.partner'
	_columns = {
        'identidad': fields.char('Numero de Identidad', help="Ingrese el numero de identidad"),
        'estado_civil' : fields.selection([('soltero','soltero'),
                                            ('casado','casado')], string='Estado Civil'),
        'fecha_nac' : fields.date('Fecha de Nacimiento', help="Indique la fecha de nacimiento"),
        'edad' : fields.char('Edad', help="Indique la Edad"),
        'sexo' : fields.selection([('m','Masculino'),
                                    ('f','Femenino')], string="Sexo"),
        'emergencia': fields.char('Telefono', help="ingrese el numero de emergencia"),
        'contacto': fields.char('Contacto',help="Persona de contacto"),
        'codigo_socio':fields.char('Codigo de Socio',help="Ingrese un codigo al socio"),

        'alto_colesterol': fields.boolean('Alto Colesterol'),
        'hipertension_arterial': fields.boolean('Hipertension Arterial'),
        'prob_coronarios': fields.boolean('Problemas Coronarios'),
        'diabetes': fields.boolean('Diabetes'),
        'asma': fields.boolean('Asma Bronquial'),
        'embarazo': fields.boolean('Embarazo'),
        'cirugias': fields.boolean('Cirugias'),
        'sobre_peso': fields.boolean('Sobre Peso'),
        'fuma': fields.boolean('Fuma'),
        'bebidas_alc': fields.boolean('Bebidas Alcholicas'),
        'contrato':fields.one2many('sale.recurring_orders.agreement','partner_id', help="Contrato asociado"),
        'estado': fields.boolean('Activo', help="Estado del cliente si esta activo o inactivo"),
	'partner':fields.many2one('res.partner','clientes',help="campor relacion con excusas"),
	'desactive_date':fields.date('Fecha de Desactivacion',help="Fecha en que se Desactivo el Cliente"),
	'active_date':fields.date('Fecha de Activacion',help="Fecha en que se Activo el cliente"),
            }


        _sql_constraints = [
        ('number_uniq', 'unique(codigo_socio)', 'El Codigo de Cliente debe Ser Unico'),

    ]

        def create(self, cr, uid, vals, context=None):
        # Si el Codigo de Socio se Encuentra vacio
            if not vals.get('codigo_socio'):
                vals['codigo_socio'] = self.pool.get('ir.sequence').get(cr, uid, 'serial_socio')
            return super(partner, self).create(cr, uid, vals, context=context)



           	

	def onchange_active(self, cr, uid, ids,estado):
		result = {}
       		date = datetime.strftime(datetime.now(), "%Y-%m-%d")
        	if estado:
			result['value'] = { 'active_date': date }
			return result
        	result['value'] = { 'desactive_date': date }
        	return result

       



	



