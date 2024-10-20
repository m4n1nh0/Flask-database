from flask import request, jsonify

from database.sessao import db
from model.transacao import Transacao


def register_routes(app):
    @app.route('/cadastrar/transacao', methods=['POST'])
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

    @app.route('/listar/transacao', methods=['GET'])
    def listar_transacao():
        transacoes = Transacao.query.all()

        # # Modo implicito
        # resultado = [{
        #         'id': transacao.id,
        #         'conta': transacao.conta,
        #         'agencia': transacao.agencia,
        #         'texto': transacao.texto,
        #         'valor': transacao.valor
        #     } for transacao in transacoes
        # ]

        # Modo tradicional
        resultados = []
        for transacao in transacoes:
            result = {
                'id': transacao.id,
                'conta': transacao.conta,
                'agencia': transacao.agencia,
                'texto': transacao.texto,
                'valor': transacao.valor
            }
            resultados.append(result)

        return jsonify(resultados), 200
