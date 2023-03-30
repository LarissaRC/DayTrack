import connexion
from flask import render_template
import agenda_user
import agenda_event

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    user = agenda_user.read_all()
    event = agenda_event.read_all()
    return render_template("home.html", user=user, event=event)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)