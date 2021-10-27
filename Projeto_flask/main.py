from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/') #rota, o que será digitado na url do navegador para ter acesso a página
# def index(): 
#     return '<h1>página index</h1> <br> <p>Conteúdo da página</p>'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login')
def login():
    return '<h1>página login</h1> <br> <p>Conteúdo da página</p>'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000) #endereço e porta onde está rodando o servidor, neste caso rodará na porta 8000 do localhost(computador local)
    
