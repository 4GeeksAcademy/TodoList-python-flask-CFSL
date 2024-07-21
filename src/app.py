# Añade el método jsonify a tu importación de Flask
from flask import Flask, jsonify, request
app = Flask(__name__)


# Supongamos que tienes tus datos en la variable some_data
#   some_data = { "name": "Bobby", "lastname": "Rixer" }
# Puedes convertir esa variable en una cadena json de la siguiente manera
#    json_text = jsonify(some_data)

#creamos una variable global todos que va a contener la lista de todos
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "cocinar", "done": True },
]

#añadir endpoints, 
#primera linea especifica el endpoint mydomain.com/myroute y el metodo que se usara con esa url
#segunda linea es una funcion
#retorno de la funcion al cliente o navegador que lo solicite
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

#añadimos nuevo endpoint
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body) #Agrega el contenido del cuerpo de la solicitud decodificada a la lista todos
    return jsonify(todos) #Devuelve la lista actualizada todos al front end, hacer jsonify

#añadimos nuevo endpoint para DELETE, recibirá la posición para eliminar en la URL de la solicitud
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)


# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)