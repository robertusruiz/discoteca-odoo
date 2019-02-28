# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class empleado(models.Model):
	_name = 'discoteca.empleado'

	name = fields.Char(string = "Nombre", required = True)
	apellidos = fields.Char(string="Apellidos", required = True)
	DNI = fields.Char(string="DNI", size = 9, required = True)
	puesto = fields.Many2one("discoteca.puesto", string="Puesto")

	@api.onchange('DNI')
	def validate_dni(self):
		if self.DNI:
			match = re.match('[1-9]{8}[BCDFGHJKLMNPQRSTVXYZ]{1}$', self.DNI)
			if match == None:
				raise ValidationError('No es un DNI valido')


class puesto(models.Model):
	_name = 'discoteca.puesto'

	name = fields.Char(string = "Tipo_puesto", required = True)
	sueldo_hora = fields.Integer(string = "Sueldo_hora", required = True)
	num_horas_mensuales = fields.Integer(string ="Numero_horas_mensuales", required = True)
	sueldo = fields.Integer(compute="_value_sueldo", store=True)

	@api.depends('sueldo_hora', 'num_horas_mensuales')
	def _value_sueldo(self):
		self.sueldo= int(self.num_horas_mensuales) * int(self.sueldo_hora)


class cliente_vip(models.Model):
	_name = 'discoteca.cliente_vip'

	name = fields.Char(string="nombre", required = True)
	apellidos = fields.Char(string="apellidos", required = True)
	DNI = fields.Char(string="DNI", size = 9,  required = True)
	entrada = fields.Many2one("discoteca.entrada", string = "entrada", required = True)

	@api.onchange('DNI')
	def validate_dni(self):
		if self.DNI:
			match = re.match('[1-9]{8}[BCDFGHJKLMNPQRSTVXYZ]{1}$', self.DNI)
			if match == None:
				raise ValidationError('No es un DNI valido')


class entrada(models.Model):
	_name = 'discoteca.entrada'

	name = fields.Integer(string = "identificador", required = True)
	tipo_entrada = fields.Selection([('0','Entrada normal'),('1','Entrada VIP')], string="Tipo_entrada", default = "0")
	precio_entrada = fields.Integer(string = "Precio_entrada", required = True)




class bono_premium(models.Model):
	_name ='discoteca.bono_premium'

	name = fields.Integer(string = "identificador", required = True)
	zona_reservada = fields.Char(string="Zona_Reservada", required = True)
	bebida = fields.Many2one("discoteca.bebida", string="bebida", required = True)
	cliente_vip = fields.Many2one("discoteca.cliente_vip", string="cliente_vip", required = True)


class bebida(models.Model):
	_name = 'discoteca.bebida'

	name = fields.Char(string = "marca", required = True)
	precio_bebida = fields.Integer(string="Precio_bebida", required = True)
	tipo_bebida = fields.Char(string="Tipo_bebida", required = True)
	graduacion = fields.Integer(string = "graduacion", required = True)
	tamaño_botella = fields.Char(string="Tamaño_botella", required = True)


class evento(models.Model):
	_name = 'discoteca.evento'

	name = fields.Integer(string = "identificador", required = True)
	nombre = fields.Char(string="Nombre", required = True)
	DJ = fields.Many2one("discoteca.dj", string="DJ", required = True)
	fecha = fields.Date(string = "Fecha", required = True)


class dj(models.Model):
	_name = 'discoteca.dj'

	name = fields.Char(string="nombre", required = True)
	apellidos = fields.Char(string="apellidos", required = True)
	DNI = fields.Char(string="DNI", required = True)
	sueldo = fields.Integer(string="sueldo", required = True)
	musica = fields.Many2one("discoteca.musica", string = "tipo_musica", required = True)

	@api.onchange('DNI')
	def validate_dni(self):
		if self.DNI:
			match = re.match('[1-9]{8}[BCDFGHJKLMNPQRSTVXYZ]{1}$', self.DNI)
			if match == None:
				raise ValidationError('No es un DNI valido')


class musica(models.Model):
	_name = 'discoteca.musica'

	name = fields.Selection([('0','Pop'),('1','Rock'),('2','Indie'), ('3','Reggaeton'), ('4','Electronica')], string = "Tipo_musica", default = "0")
