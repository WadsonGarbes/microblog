from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Wadson'}
    posts = [
        {
            'author': {'username': 'Maria'},
            'body': 'Lindo dia aqui na praia!'
        },
        {
            'author': {'username': 'José'},
            'body': 'Assistimos ao jogo do flamengo ontem!'
        }

    ]
    return render_template('index.html', title="Home", user=user, posts=posts)