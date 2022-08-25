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

- Api Root: `/api/`

- Datos Clientes: `/api/clientes/`
  (usuario común no puede acceder a estos datos)
- Datos Cliente en específico: `/api/clientes/(id-del-cliente)/` 
(usuario común puede ver solo sus datos con id)

- Cuentas: `/api/cuentas/` 
- Cuenta en específico: `/api/cuentas/(id-del-cliente)/`
- Cuentas según usuario: `/api/cuentas/?customer_id=(id)`

- Prestamos: `/api/prestamos/`
- Prestamo en específico: `/api/prestamos/(id-del-cliente)/`
- Prestamos por usuario : `/api/prestamos/?customer_id=(id)`
- Prestamo Por Sucursal: `xd`

- Sucursales: `/api/sucursales/`
  (acceso público)
- Sucursal por id: `/api/sucursales/(id-sucursal)/`

- Tarjetas: `/api/tarjetas/`
(usuario común sin acceso)
- Tarjetas por id:`/api/tarjetas/(id-tarjeta)`
- Tarjetas por cliente: `/api/tarjetas/?cliente_id=523`