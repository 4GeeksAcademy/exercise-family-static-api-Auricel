"""
Este módulo se encarga de iniciar el servidor API, cargar la base de datos y agregar los puntos finales.
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# crear el objeto de la familia jackson
jackson_family = FamilyStructure("Jackson")

john = {
    "first_name": "John",
    "last_name": jackson_family.last_name, #(para sea dinamico) 
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}

jane = {
    "first_name": "Jane",
    "last_name": jackson_family.last_name,
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}

jimmy = {
    "first_name": "Jimmy",
    "last_name": jackson_family.last_name,
    "age": 5,
    "lucky_numbers": [1]
}

jackson_family.add_member(john)
jackson_family.add_member(jane)
jackson_family.add_member(jimmy)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generar un mapa del sitio con todos sus puntos finales
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():

    # Así es como puedes usar la estructura de datos Familia llamando a sus métodos
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
     member = jackson_family.get_member(member_id)
     if member:
         return jsonify(member), 200
     return jsonify({"msg": "Miembro no encontrado"}), 400

    

@app.route('/member', methods=['POST'])
def add_member():

    new_member = request.json
    
    jackson_family.add_member(new_member)
    
    return jsonify({"done":"usuario creado"}), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    eliminar_familiar = jackson_family.delete_member(member_id)
    
    if not eliminar_familiar:
        return jsonify({"msg": "familiar no encontrado"}), 400
    return jsonify({"done": True}), 200




# Esto solo se ejecuta si se ejecuta `$ python src/app.py`
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
