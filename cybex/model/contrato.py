# -*- coding: utf-8 -*-
from openerp.osv import fields, osv





class contrato(osv.Model):

	_name = 'cybex.contrato_membresia'

	_columns = {
            'name': fields.char('Numero de Contrato', help="Ingrese el Numero de Contrato"),
            'tipo_membresiaids': fields.many2one('product.product','Tipos de Membresia',
            help="Elija el tipo de membresia que asignara al contrato"),
            'fecha_inicio': fields.date('Fecha de Inicio de el contrato',
                help="Porfavor indique cuando inicia el contrato"),
            'fecha_fin': fields.date('Fecha de Finalizacion de el contrato',
                help="Porfavor indique cuando Finaliza el contrato"),
            'valor_inscripcion': fields.float('Valor de la Inscripcion(LPS)', help="Ingrese el valor de la inscripcion"),
             'usuario_id': fields.many2one('res.users', 'Vendedor',
            help="Seleccione el Nombre del Vendedor"),
            'observaciones': fields.text('Observaciones', help="Observaciones"),
            'socios_ids': fields.one2many('cybex.socios', 'contrato_membresia_id', 'Socios',
            help="Ingrese Los Socios Que Seran Parte del Contrato"),

            'state' : fields.selection([('inactivo','inactivo'),
                                           ('pagado','pagado')], string="State"),

            }

        _sql_constraints = [('date_interval_check','CHECK(fecha_fin >=fecha_inicio)','la fecha final debe ser mayor que la inicial')]

        _defaults = {
        'state': 'inactivo',
        }

        def action_draft(self, cr, uid, ids, context=None):
            return self.write(cr, uid, ids, {'state':'inactivo'}, context=context)


        def action_done(self, cr, uid, ids, context=None):
            return self.write(cr, uid, ids, {'state':'pagado'}, context=context)

