from database.sessao import db


class Transacao(db.Model):
    __tablename__ = 'transacao'
    id = db.column(db.Integer, primary_key=True)
    conta = db.column(db.String(20), nullable=False)
    agencia = db.column(db.String(10), nullable=False)
    texto = db.column(db.String(), nullable=True)
    valor = db.column(db.Float(), nullable=False)
    