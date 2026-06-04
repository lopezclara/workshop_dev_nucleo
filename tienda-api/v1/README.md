```
Endpoints Disponibles por Versión
v1: API Básica
Método	Endpoint	Descripción	Parámetros	Ejemplo
GET	/	Información general de la app	—	curl http://localhost:8080/
GET	/productos	Lista todos los productos	—	curl http://localhost:8080/productos
GET	/productos/<id>	Detalle de un producto específico	id: ID del producto (int)	curl http://localhost:8080/productos/1
GET	/version	Info de versión y host	—	curl http://localhost:8080/version
GET	/health	Health check	—	curl http://localhost:8080/health
GET	/stress	Genera carga de CPU (HPA demo)	seconds: duración en segundos (max 30)	curl http://localhost:8080/stress?seconds=10
```
