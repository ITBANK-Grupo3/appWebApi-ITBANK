from .models import Direcciones
class MyRouter:

    def db_for_read(self, model, **hints):
        if model == Direcciones:
            return 'homebanking'

    def db_for_write(self, model, **hints):
        if model == Direcciones:
            return 'homebanking'
