from django.contrib import admin
from database.models import Cuenta,Direcciones,Empleado,Movimientos,Prestamo,Sucursal,MarcaTarjeta,Tarjeta,TipoCliente,TipoCuenta,Cliente

# Register your models here.

class CuentaAdmin(admin.ModelAdmin):
    list_display=("customer_id","balance","tipo_cuenta")
    search_fields=("customer_id","tipo_cuenta")

class DireccionesAdmin(admin.ModelAdmin):
    list_display=("customer_id","calle","numero","ciudad","provincia","pais")
    search_fields=("customer_id","calle","numero","ciudad","provincia","pais")
    list_filter=("ciudad","provincia","pais")

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=("employee_name","employee_surname","employee_hire_date","employee_dni","branch_id")
    search_fields=("employee_name","employee_surname","employee_dni","branch_id")
    list_filter=("employee_hire_date","branch_id")

class MovimientosAdmin(admin.ModelAdmin):
    list_display=("account_id","account_id_rec","amount","type","created_at")
    search_fields=("account_id","account_id_rec","type")

class PrestamoAdmin(admin.ModelAdmin):
    list_display=("loan_type","loan_date","loan_total","customer_id")
    search_fields=("loan_type","customer_id")
    list_filter=("loan_date","loan_type")

class SucursalAdmin(admin.ModelAdmin):
    list_display=("branch_id","branch_name","branch_address_id")
    search_fields=("branch_name","branch_address_id")

class MarcaTarjetaAdmin(admin.ModelAdmin):
    list_display=("marca_tarjeta_id","marca_tarjeta_nombre")
    
class TarjetaAdmin(admin.ModelAdmin):
    list_display=("numero_tarjeta","cvv","fecha_creacion","fecha_vencimiento","tipo_tarjeta","cliente_id","marca_tarjeta_id")
    search_fields=("numero_tarjeta","fecha_creacion")
    list_filter=("fecha_creacion","tipo_tarjeta","marca_tarjeta_id")

class TipoClienteAdmin(admin.ModelAdmin):
    list_display=("tipo_id","nombre_tipo")

class TipoCuentaAdmin(admin.ModelAdmin):
    list_display=("tipo_id","nombre_tipo")

class ClienteAdmin(admin.ModelAdmin):
    list_display=("customer_id","customer_name","customer_surname","customer_dni","dob","branch_id")
    search_fields=("customer_id","customer_name","customer_surname","customer_dni","branch_id")

admin.site.register(Cuenta,CuentaAdmin)
admin.site.register(Direcciones,DireccionesAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Movimientos,MovimientosAdmin)
admin.site.register(Prestamo,PrestamoAdmin)
admin.site.register(Sucursal,SucursalAdmin)
admin.site.register(MarcaTarjeta,MarcaTarjetaAdmin)
admin.site.register(Tarjeta,TarjetaAdmin)
admin.site.register(TipoCliente,TipoClienteAdmin)
admin.site.register(TipoCuenta,TipoCuentaAdmin)
admin.site.register(Cliente,ClienteAdmin)
