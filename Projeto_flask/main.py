from flask import Flask
app = Flask(__name__)

@app.route('/index') #rota, o que será digitado na url do navegador para ter acesso a página
def index(): 
    return '<h1>página index</h1> <br> <p>Conteúdo da página</p>'

@app.route('/login')
def login():
    return '<h1>página login</h1> <br> <p>Conteúdo da página</p>'

@app.route('/home')
def home():
    return '<h1>página Home</h1> <br> <p>Conteúdo da página</p>'

@app.route('/form')
def form():
    return '<h3>Página Formuário</h3> <br> <p><b>Conteúdo da página</b></p> <form> <input type="text" id="nome" /> <label for="nome">Nome:</label>  </form>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000) #endereço e porta onde está rodando o servidor.
