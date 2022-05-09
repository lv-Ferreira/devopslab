from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Oi! eu sou o Leonardo Vinicius e essa é a minha mensagem customizada!"

if __name__ == '__main__':
    app.run()