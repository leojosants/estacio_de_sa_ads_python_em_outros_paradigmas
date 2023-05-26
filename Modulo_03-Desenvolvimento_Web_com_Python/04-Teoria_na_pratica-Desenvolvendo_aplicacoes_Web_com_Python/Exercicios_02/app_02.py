from flask import Flask

app = Flask(__name__)


@app.route('/')
def cumprimento():
    boas_vindas = '<h1>Olá, programadores!</h1>'
    link = '<p><a href="user/usuario">Clique aqui!</a></p>'
    return boas_vindas + link


@app.route('/user/')
@app.route('/user/<nome>')
def user(nome="Usuário"):
    personalizar = f'<h1>Olá, {nome}!</h1>'
    instrucao = "<p>No link 'http://localhost:5000/user/usuario' altere o nome '<em>usuario</em>' e recarregue a página!</p>"
    return personalizar + instrucao


if __name__ == '__main__':
    app.run(debug=True)
