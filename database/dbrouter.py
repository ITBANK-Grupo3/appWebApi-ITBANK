from .models import Cuenta,Direcciones,Empleado,Movimientos,Prestamo,Sucursal,MarcaTarjeta,Tarjeta,TipoCliente,TipoCuenta,Cliente
models = [Cuenta,Direcciones,Empleado,Movimientos,Prestamo,Sucursal,MarcaTarjeta,Tarjeta,TipoCliente,TipoCuenta,Cliente]
class MyRouter:

    def db_for_read(self, model, **hints):
        if model in models:
            return 'homebanking'

    def db_for_write(self, model, **hints):
        if model in models:
            return 'homebanking'
