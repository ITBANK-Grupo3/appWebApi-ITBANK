## Falta!
**api domicilios!**


## HomeBanking - ITBANK
## **Importante!**
Instalar los paquetes cargados en el `requirements.txt`

## Registrarse en el banco
Si el Dni cargado al momento del registro se encuentra en la tabla de empleados, el usuario se creará como parte del staff y se le permitirá navegar libremente por la API. De lo contrario, el usuario solo podrá acceder a los datos pertenecientes a su usuario, y a la api de sucursales

**Datos de usuario Admin:**
- Usuario: "admin"
- Contraseña: 000
## Documentación de la API
Debe estar autorizado en el banco para poder navergar por el menú

**Root**
- Api Root: `/api/`

**Clientes**
- Datos Clientes: `/api/clientes/`
  (usuario común no puede acceder a estos datos)
- Datos Cliente en específico: `/api/clientes/(id-del-cliente)/` 
(usuario común puede ver solo sus datos con id)

**Cuentas**
- Cuentas: `/api/cuentas/` (al usuario común solo se cargan sus cuentas y no funcionan filtros)
- Cuenta en específico: `/api/cuentas/(id-del-cliente)/`
- Cuentas según usuario: `/api/cuentas/?customer_id=(id)`

**Prestamos**
- Prestamos: `/api/prestamos/` (al usuario común solo se cargan sus prestamos y no funcionan filtros)
- Prestamo en específico: `/api/prestamos/(id-del-cliente)/`
- Prestamos por usuario : `/api/prestamos/?customer_id=(id)`
- Prestamos por Sucursal: `/api/prestamos/?sucursal_id=(id)`

**Sucursales**
- Sucursales: `/api/sucursales/`
  (acceso público)
- Sucursal por id: `/api/sucursales/(id-sucursal)/`

**Tarjetas**
- Tarjetas: `/api/tarjetas/`
(usuario común sin acceso)
- Tarjetas por id:`/api/tarjetas/(id-tarjeta)`
- Tarjetas por cliente: `/api/tarjetas/?cliente_id=523`