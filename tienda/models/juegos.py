from odoo import models, fields, api

class Juego(models.Model):
    _name = 'tienda.juegos'
    codigo = fields.Char(string='Codigo', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    rangoEdad = fields.Char(string='RangoEdad', required=True)
    stockJuego = fields.Integer(string='StockJuego', required=True)
    precioJuego = fields.Integer(string='Precio', required=True)
