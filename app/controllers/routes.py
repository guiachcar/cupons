from app import app
from app.models.tables import Cupom

from flask import request, jsonify

@app.route('/cupoms', methods=['GET'])
def cupoms_listar():
    cupoms = Cupom.query.all()
    output = []
    for cupom in cupoms:
        cupom_data = {}
        cupom_data['nome'] = cupom.nome
        cupom_data['email'] = cupom.email
        cupom_data['valor'] = cupom.valor
        output.append(cupom_data)
    return jsonify({'cupoms' : output})

@app.route('/cupoms', methods=['POST'])
def cupom_cadastrar():
    data = request.get_json()
    cupom = Cupom(nome=data['nome'], email=data['email'], valor=data['valor'])
    cupom.save()
    return jsonify(data),201


