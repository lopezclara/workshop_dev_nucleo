import time
from flask import Flask, Response
app = Flask(__name__)

start_time = time.time()

@app.route('/')
def index():
    return "App con Probes lista.\n"

@app.route('/healthz')
def healthz():
    # Simula que la app falla después de 60 segundos de vida
    #if time.time() - start_time > 60:
    #    return Response("Fallo interno", status=500)
    return "OK", 200

@app.route('/ready')
def ready():
    # Endpoint simple para readiness
    return "Listo v4 - Test webhook u995238", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
