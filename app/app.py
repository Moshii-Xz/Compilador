import sys
import os
from flask import Flask, render_template, request, jsonify

# Agrega el directorio 'compiler' al sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'compiler'))

import access  # Ahora debería encontrar el módulo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.form['code']
    try:
        # Ejecuta el compilador con el código proporcionado
        output = access.execute(code)
    except Exception as e:
        # Captura cualquier error que ocurra durante la compilación/ejecución
        output = f"Error: {str(e)}"
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
