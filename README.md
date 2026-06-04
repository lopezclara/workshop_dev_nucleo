WorkShop Dev Nucleo
```
[Route OCP]
     ↓
 pedido-api (entrada)
   ├─ GET /productos/{id} → producto-api
   ├─ PUT /productos/{id}/stock → producto-api  
   └─ POST /notificaciones → notificacion-api
                              ↓
                          PostgreSQL 16
```

Stack Tecnico
```
Componente	Versión
Runtime	Quarkus 3.15.1 + Java 21
REST Server	quarkus-rest + quarkus-rest-jackson
REST Client	quarkus-rest-client-jackson
ORM	Hibernate ORM Panache
BD	PostgreSQL 16
Tracing	quarkus-opentelemetry (OTLP/gRPC)
Métricas	Micrometer + Prometheus
Logging	JSON Logging
Health	SmallRye Health
```

Microservicios
```
Endpoint: GET /productos/{id}
Endpoint: PUT /productos/{id}/stock (actualizar stock)
Persiste en tabla productos
Cliente REST: ninguno (solo recibe llamadas)
2. pedido-api (Orquestador)
Endpoint: POST /pedidos (entrada principal)
Llamador de producto-api y notificacion-api
Persiste en tabla pedidos
Clientes REST:
ProductoClient → producto-api
NotificacionClient → notificacion-api
3. notificacion-api (Notificaciones)
Endpoint: POST /notificaciones
Persiste en tabla notificaciones
Cliente REST: ninguno (solo recibe llamadas)
```

Endpoints disponibles
```
Método	Endpoint	Descripción
GET	/productos	Listar todos los productos
GET	/productos/{id}	Obtener producto por ID
POST	/productos	Crear nuevo producto
PUT	/productos/{id}/stock	Actualizar stock
GET	/pedidos	Listar todos los pedidos
GET	/pedidos/{id}	Obtener pedido por ID
POST	/pedidos	Crear pedido (genera traza completa)
PUT	/pedidos/{id}/estado	Cambiar estado del pedido
GET	/notificaciones	Listar notificaciones
POST	/notificaciones	Registrar notificación
```

Pruebas
1. POST /productos - Crear 2-3 productos
```
curl -X POST http://localhost:8080/productos \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Laptop Dell XPS 13",
    "descripcion": "Portátil ultraligero de alta gama",
    "precio": 1299.99,
    "stock": 50
  }'
```
Consultar producto
```
curl -X GET http://localhost:8080/productos/1
```

2. POST /pedidos - Crear varios pedidos (observa trazas en Jaeger)
```
curl -X POST http://localhost:8080/pedidos \
  -H "Content-Type: application/json" \
  -d '{
    "productoId": 1,
    "cantidad": 2,
    "clienteNombre": "Juan García"
  }'
```
3. GET /notificaciones - Verifica que se registraron
```
curl -X GET http://localhost:8080/notificaciones
```

4. PUT /pedidos/{id}/estado - Cambia estado a CONFIRMADO
```
curl -X PUT http://localhost:8080/pedidos/1/estado \
  -H "Content-Type: application/json" \
  -d '{
    "estado": "CONFIRMADO"
  }'
```
Abre Jaeger - Visualiza las trazas distribuidas con los traces-IDs propagados
