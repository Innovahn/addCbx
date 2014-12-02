# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class excusa(osv.Model):

    _name = 'excusa'



    def _obtener_clientes(self,cr,uid,id,field,args,context=None):
	print "*"*50
	print id
	nombres=[]
	unidad=''	
	res={}
	for obj_excusa in self.browse(cr,uid,id,context=context):
	    nombres=[]
	    for clientes in obj_excusa.clientes:
		print "/"*50
		
		
		unidad=clientes.partner_id.name
       		nombres.append(unidad)
		
	    res[obj_excusa.id]=nombres
	    print nombres
	return res

    def _obtener_codigos(self,cr,uid,id,field,args,context=None):
	print "*"*50
	print id
	codigos=[]
	unidad=''	
	res={}
	for obj_excusa in self.browse(cr,uid,id,context=context):
	    codigos=[]
	    for codigo in obj_excusa.clientes:
		print "/"*50
		
		
		unidad=codigo.partner_id.codigo_socio
       		codigos.append(unidad)
		
	    res[obj_excusa.id]=codigos
	    
	return res	
	


    _columns = {
	    'csocio':fields.function(_obtener_codigos,string='Codigos',type="char"),
	    'nombres_clientes':fields.function(_obtener_clientes,string='Clientes Excusados',type="char"),	
            'name':fields.char('n°',help="Numero de excusa"),
            'fecha_creacion':fields.date('Fecha de Firma',select=1,help="fecha en que firmo la excusa"),
            'fecha_inicio':fields.date('Fecha Inicio',help="Fecha de inicio de Excusa"),
            'fecha_final':fields.date('Fecha de Finalizacion',help="fecha de finalizacion, en caso de ser indefinida dejar en blanco"),
            'descripcion':fields.text('Razon de Excusa',help="Razon por la cual fue creada la excusa"),
            'receptor':fields.many2one('res.users','receptor',help="Persona que recibe la excusa"),
            'clientes':fields.one2many('socios','contrato_id',"Clientes",help="Clientes a los cuales afecta la excusa"),
            'recurrente_id': fields.many2one('sale.recurring_orders.agreement'),
	    'observaciones':fields.text('Observaciones',help="Ingrese las observaciones que tenga sobre la Excusa"),
        }


