from odoo import models, fields, api

class Clientes(models.Model):
    _name = 'tienda.clientes'
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    nif = fields.Char(string='NIF', required=True)
    telefono = fields.Char(string='Telefono')
    juego = fields.Many2many('tienda.juegos', string='juego')
