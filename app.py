from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Oi! eu sou o Leonardo Vinicius e essa é a minha mensagem customizada!"

if __name__ == '__main__':
    app.run()