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

    # Listar transações com filtros
    @app.route('/transacao/filtro', methods=['GET'])
    def listar_transacoes_com_filtros():
        conta = request.args.get('conta')
        agencia = request.args.get('agencia')
        query = Transacao.query

        if conta:
            query = query.filter_by(conta=conta)
        if agencia:
            query = query.filter_by(agencia=agencia)

        transacoes_filtradas = query.all()
        resultado = [
            {
                'id': transacao.id,
                'conta': transacao.conta,
                'agencia': transacao.agencia,
                'texto': transacao.texto,
                'valor': transacao.valor
            } for transacao in transacoes_filtradas
        ]
        return jsonify(resultado), 200

    # Atualizar uma transação
    @app.route('/transacao/<int:id>', methods=['PUT'])
    def atualizar_transacao(id):
        data = request.get_json()
        transacao = Transacao.query.get_or_404(id)

        transacao.conta = data.get('conta', transacao.conta)
        transacao.agencia = data.get('agencia', transacao.agencia)
        transacao.texto = data.get('texto', transacao.texto)
        transacao.valor = data.get('valor', transacao.valor)

        db.session.commit()

        return jsonify({'message': 'Transação atualizada com sucesso!'}), 200

    # Deletar uma transação
    @app.route('/transacao/<int:id>', methods=['DELETE'])
    def deletar_transacao(id):
        transacao = Transacao.query.get_or_404(id)

        db.session.delete(transacao)
        db.session.commit()

        return jsonify({'message': 'Transação deletada com sucesso!'}), 200
