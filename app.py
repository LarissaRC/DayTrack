import sqlite3
import querys
from flask import Flask, session, render_template, request, g, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "greenwhaleonthesky"
app.config["SESSION_COOKIE_NAME"] = "catsleepsonthetree45"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]
        
        user_id = querys.get_user(user_email, user_password)
        if(user_id):
            session["user_id"] = user_id
            session.modified = True
            return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/signgup", methods=["GET", "POST"])
def logup():
    if request.method == "POST":
        user_name = request.form["user_name"]
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]
        querys.register_user(user_name, user_email, user_password)
        user_id = querys.get_user(user_email, user_password)

        if(user_id):
            session["user_id"] = user_id
            session.modified = True
            return redirect(url_for("login"))
    else:
        return render_template("logup.html")

@app.route("/home", methods=["GET"])
def home():
    user_id = session["user_id"]
    codigos, titulos, descricoes, anos, meses, dias = querys.get_events(user_id)
    eventos = []
    
    for i in range(len(codigos)):
        eventos.append((codigos[i], titulos[i], descricoes[i], anos[i], meses[i], dias[i]))

    session["eventos"] = eventos
    session.modified = True

    return render_template("home.html", eventos = session["eventos"])

if __name__ == '__main__':
    app.run()