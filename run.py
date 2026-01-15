# Arquivo principal para iniciar a aplicação

from src.app import app

# Executa o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
