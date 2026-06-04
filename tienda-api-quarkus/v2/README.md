
v2: Con Paginación y Filtrado
Incluye todos los de v1, más mejoras:

Método	Endpoint	Descripción	Parámetros	Ejemplo
```
GET	/	Información con mención de paginación	—	curl http://localhost:8080/
GET	/productos	Lista con paginación y filtrado	page: número página (default 1)

curl "http://localhost:8080/productos?page=1&limit=5"

curl "http://localhost:8080/productos?categoria=perifericos"
GET	/productos/<id>	Igual que v1	—	—
GET	/version	Incluye lista de features nuevas	—	—
GET	/health	Igual que v1	—	—
GET	/stress	Igual que v1	—	—
```
### Categorías disponibles en v2/v3:
computacion
monitores
perifericos
audio
video
accesorios
almacenamiento
