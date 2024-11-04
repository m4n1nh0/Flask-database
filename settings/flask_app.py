from flask import Flask

from database.sessao import db
from routes.transacao import register_routes
from settings.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all() #Criar todas as tabelas

    register_routes(app)

    return app
