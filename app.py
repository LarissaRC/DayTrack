import sqlite3
from flask import Flask, session, render_template, request, g, flash

app = Flask(__name__)
app.secret_key = "greenwhaleonthesky"
app.config["SESSION_COOKIE_NAME"] = "catsleepsonthetree45"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signgup")
def logup():
    return render_template("logup.html")

@app.route("/home", methods=["get"])
def home():
    codigos, titulos, descricoes, anos, meses, dias = get_db_eventos()
    eventos = []
    for i in range(len(codigos)):
        eventos.append((codigos[i], titulos[i], descricoes[i], anos[i], meses[i], dias[i]))

    session["eventos"] = eventos
    session.modified = True

    return render_template("home.html", eventos = session["eventos"])

def get_db_eventos():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('agenda.db')
        cursor = db.cursor()
        cursor.execute("select * from Evento")
        all_data = cursor.fetchall()
        codigos = [str(val[0]) for val in all_data]
        titulos = [str(val[1]) for val in all_data]
        descricoes = [str(val[2]) for val in all_data]
        datas = [str(val[3]) for val in all_data]
        anos = [val[:4] for val in datas]
        meses = [val[5:7] for val in datas]
        dias = [val[8:10] for val in datas]

    return codigos, titulos, descricoes, anos, meses, dias

def get_db_users(email, senha):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('agenda.db')
        cursor = db.cursor()
        cursor.execute("select * from User where email='" + email + "' and senha='" + senha + "'")
        user = cursor.fetchall()

    return user

if __name__ == '__main__':
    app.run()