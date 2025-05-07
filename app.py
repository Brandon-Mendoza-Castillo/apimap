from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from tsp_solver import calcular_ruta, coord

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html', ciudades=coord)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    seleccionadas = data.get('ciudades')
    if not seleccionadas:
        return jsonify({'error': 'No hay ciudades seleccionadas'}), 400

    ciudades_filtradas = {k: coord[k] for k in seleccionadas}
    ruta, distancia = calcular_ruta(ciudades_filtradas)
    coordenadas = [coord[ciudad] for ciudad in ruta]

    return jsonify({
        'ruta': ruta,
        'coordenadas': coordenadas,
        'distancia': round(distancia, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
