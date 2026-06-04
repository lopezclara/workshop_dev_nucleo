```
v3: Logging Estructurado + Headers de Correlación
Incluye todos los de v2, más:

Método	Endpoint	Descripción	Parámetros	Headers Especiales
GET	/	Mensaje menciona logging + correlation ID	—	Devuelve X-Correlation-ID
GET	/productos	Igual v2, con logs JSON	—	Devuelve X-Correlation-ID
GET	/productos/<id>	Igual v2, con logs de búsqueda fallida	—	Devuelve X-Correlation-ID
GET	/version	Igual v2	—	Devuelve X-Correlation-ID
GET	/health	Igual v2	—	Devuelve X-Correlation-ID
GET	/stress	Igual v2, con logs de inicio/fin	—	Devuelve X-Correlation-ID
GET	/error-demo	NUEVO: Genera excepción para demo de error logging	—	Devuelve X-Correlation-ID
```

Headers

Request:
  X-Correlation-ID: [opcional] ID de correlación (si no viene, se genera)

Response:
  X-Correlation-ID: [devuelto] ID para trazabilidad
Ejemplo con correlacion:

# Sin proporcionar ID (se genera automáticamente)
curl http://localhost:8080/productos

# Proporcionando ID (propagado a través de servicios)
curl -H "X-Correlation-ID: req-12345-xyz" http://localhost:8080/productos
Obtener perifericos de pagina 2

curl "http://localhost:8080/productos?categoria=perifericos&page=2&limit=5"
HPA

curl "http://localhost:8080/stress?seconds=15"
Prueba categoria

curl -H "X-Correlation-ID: workshop-123" \
  "http://localhost:8080/productos?categoria=computacion"
# En los logs verás: "correlation_id": "workshop-123"
Prueba error

curl http://localhost:8080/error-demo
# Verá excepción con traceback en stderr (formato JSON)
