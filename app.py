import connexion
from flask import Flask, render_template, request, session, redirect, url_for
from backend import db_user_query

#app = connexion.App(__name__, specification_dir="./")
#app.add_api("swagger.yml")

app = Flask(__name__)
app.secret_key = "greenwhaleonthesky"
#app.config["SESSION_COOKIE_NAME"] = "catsleepsonthetree45"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]
        
        user_id = db_user_query.verify_user_email(user_email)
        if user_id is not None:
            user_name = db_user_query.verify_user_password(user_id, user_password)
            if user_name is not None:
                session["user_id"] = user_id
                session.modified = True
                return redirect(url_for("home"))
            else:
                print("Senha incorreta!")
        else:
            print("Email inexistente ou incorreto!")
    else:
        return render_template("login.html")

@app.route("/signgup", methods=["GET", "POST"])
def logup():
    if request.method == "POST":
        user_name = request.form["user_name"]
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]

        user_id = db_user_query.verify_user_email(user_email)
        if user_id is not None:
            print("Usuário já existente!")
            return render_template("logup.html")
        else:
            print("Usuário não existe e pode ser cadastrado!")
            db_user_query.add_user((user_name, user_email, user_password, 0))
        
            return redirect(url_for("login"))
    else:
        return render_template("logup.html")

@app.route("/home", methods=["GET"])
def home():
    user_id = session["user_id"]

    eventos = db_user_query.get_user_events(user_id, True)
    user_name = db_user_query.get_user_name(user_id)

    print(eventos)

    session["eventos"] = eventos
    session["user_name"] = user_name
    session.modified = True

    return render_template("home.html", eventos = session["eventos"], user_name = session["user_name"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)