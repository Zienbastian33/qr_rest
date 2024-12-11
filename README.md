# RestQR - Sistema Digital de Menú y Pedidos

RestQR es una aplicación web moderna diseñada para restaurantes que permite la gestión digital de menús y pedidos a través de códigos QR. El sistema facilita tanto los pedidos locales como los pedidos para delivery, mejorando la eficiencia operativa del restaurante.

## 🚀 Características Principales

### 📱 Menú Digital
- **Acceso vía QR**: Cada mesa tiene su código QR único
- **Menú Interactivo**: Visualización atractiva de platos con imágenes
- **Categorías**: Organización clara del menú (Handrolls, Gohan, Bebidas, Extras)
- **Carrito de Compras**: Sistema intuitivo para agregar y modificar pedidos
- **Sesiones Individuales**: Cada mesa/cliente tiene su propio carrito de compras

### 👨‍💼 Panel de Administración
- **Generador de QR**:
  - Creación de códigos QR únicos por mesa
  - Gestión de tokens y códigos de activación
  - Vista de URLs completas para cada QR
- **Gestión de Mesas**:
  - Activación/desactivación de mesas
  - Monitoreo de sesiones activas
  - Control de estado de las mesas

### 👨‍🍳 Vista de Cocina
- **Panel Dividido**:
  - Columna para pedidos locales
  - Columna para pedidos delivery (en desarrollo)
- **Gestión de Pedidos**:
  - Visualización en tiempo real
  - Detalles completos de cada pedido
  - Sistema de marcado de pedidos completados
- **Actualizaciones Automáticas**:
  - Refresco automático cada 30 segundos
  - Reloj en tiempo real
  - Eliminación automática de pedidos completados

### 🔒 Seguridad
- Validación de tokens para acceso al menú
- Sistema de códigos de activación para mesas
- Protección de rutas administrativas
- Sesiones individuales para cada cliente

## 🔄 Historial de Desarrollo

### Última Sesión (10/12/2024)

#### Mejoras en la Gestión de Mesas
1. **Sistema de Activación de Mesas**
   - Implementación de tokens únicos por mesa
   - Códigos de activación de 6 dígitos
   - Validación de sesiones activas
   - Control de duración de sesiones (1-4 horas)

2. **Panel de Administración Mejorado**
   - Vista en tiempo real de mesas activas
   - Interfaz para activación/desactivación de mesas
   - Visualización de tiempos de inicio y fin de sesión
   - Actualización automática cada 30 segundos

3. **Vista de Cocina**
   - Panel dividido para pedidos locales y delivery
   - Actualización en tiempo real de pedidos
   - Sistema de marcado de pedidos completados
   - Filtrado automático por tipo de pedido

4. **Correcciones y Optimizaciones**
   - Arreglo del sistema de carrito por sesión
   - Corrección de errores en la desactivación de mesas
   - Mejora en el manejo de errores y mensajes al usuario
   - Optimización de consultas a la base de datos

### Stack Tecnológico Actualizado
- **Backend**: Flask 2.0.1
- **ORM**: Flask-SQLAlchemy 2.5.1
- **Migraciones**: Flask-Migrate 3.1.0
- **Frontend**: Bootstrap 5, JavaScript vanilla
- **Base de Datos**: SQLAlchemy con SQLite
- **Autenticación**: Sistema personalizado de tokens

### Estructura de la Base de Datos
```sql
# Principales Modelos

MenuItem:
  - id (PK)
  - name
  - description
  - price
  - category
  - available (boolean)

Order:
  - id (PK)
  - table_number
  - status
  - timestamp
  - total
  - is_delivery
  - delivery_address
  - customer_phone

TableToken:
  - id (PK)
  - table_number
  - token
  - activation_code
  - session_active
  - session_start
  - session_end
  - is_active
  - created_at
  - last_used
```



## 🚀 Instalación y Configuración

1. Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd proyecto_restqr
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```


4. Inicializar la base de datos:
```bash
flask db upgrade
```

5. Ejecutar la aplicación:
```bash
flask run
o
python run.py
```

## 🎯 Uso del Sistema

### Para Clientes
1. Escanear el código QR de la mesa
2. Navegar por el menú digital
3. Agregar items al carrito
4. Confirmar el pedido

### Para Administradores
1. Acceder al panel de administración
2. Generar códigos QR para las mesas
3. Monitorear pedidos activos
4. Gestionar estados de las mesas

### Para la Cocina
1. Acceder a la vista de cocina
2. Visualizar pedidos entrantes
3. Ver detalles de cada pedido
4. Marcar pedidos como completados

## 📝 Notas Adicionales
- El sistema se ha diseniado por defecto para un restaurante de sushi pero es adaptable a cualquier tipo de restaurante
- Interfaz responsive que se adapta a diferentes dispositivos
- Sistema de actualización en tiempo real para la cocina
- Diseño moderno y fácil de usar

## 🤝 Contribuir
Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE.md para más detalles.
