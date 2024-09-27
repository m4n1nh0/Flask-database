from flask import request, jsonify

from database.sessao import db
from model.transacao import Transacao


def register_routes(app):
    @app.route('/transacao', methods=['POST'])
    def criar_transacao():
        data = request.get_json()

        nova_transacao = Transacao(
            conta=data.get('conta'),
            agencia=data['agencia'],
            texto=data.get('texto', None),
            valor=data['valor']
        )

        db.session.add(nova_transacao)
        db.session.commit()

        return jsonify({'mensagem': 'Transacao realizada'}), 200
