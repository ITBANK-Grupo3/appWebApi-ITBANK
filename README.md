## HomeBanking - ITBANK
**Datos de usuario Admin:**
- Usuario: "admin"
- Contraseña: 000

**Registrarse en el banco**
Si el Dni cargado al momento del registro se encuentra en la tabla de empleados, el usuario se creará como parte del staff y se le permitirá navegar libremente por la API. De lo contrario, el usuario solo podrá acceder a los datos pertenecientes a su usuario, y a la api de sucursales

## Documentación de la API
Debe estar autorizado en el banco para poder navergar por el menú

- Api Root: `http://localhost:8000/api/`

- Datos Clientes: `http://localhost:8000/api/clientes/`
  (usuario común no puede acceder a estos datos)
- Datos Cliente en específico: `http://localhost:8000/api/clientes/(id-del-cliente)/`

- Cuentas: `http://localhost:8000/api/cuentas/` 
  (al usuario común solo se le carga sus cuentas)
- Cuenta en específico: `http://localhost:8000/api/cuentas/(id-del-cliente)/`

- Prestamos: `http://localhost:8000/api/prestamos/`
  (al usuario común solo se le carga sus prestamos)
- Prestamo en específico: `http://localhost:8000/api/prestamos/(id-del-cliente)/`

- Sucursales: `http://localhost:8000/api/sucursal_prestamos/`
  (acceso a usuario autenticado)
- Prestamos por sucursal: `http://localhost:8000/api/sucursal_prestamos/(id-sucursal)/`