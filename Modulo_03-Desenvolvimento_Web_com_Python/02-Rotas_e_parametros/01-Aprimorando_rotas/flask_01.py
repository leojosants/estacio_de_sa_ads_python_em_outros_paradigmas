from flask import Flask

app = Flask(__name__)  # type: ignore


@app.route('/')
def ola_mundo():
    return "Olá, mundo!"


if __name__ == '__main__':
    app.run()
