"""
Arquivo responsável por criar a aplicação Flask
e registrar as rotas do sistema.
"""

from flask import Flask
from .routes import main

# Criação da aplicação
app = Flask(__name__)

# Chave para sessões (Otimo para práticas de segurança)
app.secret_key = "secret_key"

# Registro do blueprint de rotas
app.register_blueprint(main)


