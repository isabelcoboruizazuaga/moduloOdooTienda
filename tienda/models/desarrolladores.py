from odoo import models, fields, api

class Desarrolladores(models.Model):
    _name = 'tienda.desarrolladores'
    id = fields.Char(string='Identificador', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    nif = fields.Char(string='NIF', required=True)
    nombreMarca= fields.Char(string='NombreMarca', required=True)
    juego = fields.Many2many('tienda.juegos', string='Juego')
