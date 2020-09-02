import flask
from flask import request,jsonify, render_template

app = flask.Flask(__name__, template_folder="templates")

miasta = ["Warszawa","Krakow","Kielce"]

osoby = [
    {"imie":"Marek",
     "wiek":20},
    {"imie": "Ola",
     "wiek": 18},
    {"imie": "Jaroslaw",
     "wiek": 90},
]

klucze=["haslo","pizza","ryba","ga09HjP879"]

@app.route("/",methods=["POST","GET"])
def index():
    return render_template("index.html")

@app.route("/username/<string:user>")
def usr(user):
    return render_template("username.html", username=user)

@app.route("/listy")
def listy():
    return render_template("listy.html", miasta = miasta)

@app.route("/dajkwote",methods=["POST","GET"])
def dajkwote():
    if request.method == "POST":
        kwota = request.form['kwotainput']
        return render_template("dajkwote.html", kwota=kwota)
    else:
        return render_template("dajkwote.html", kwota="None provider")

@app.route("/api/<int:minwiek>")
def wiek(minwiek):
    return jsonify([x for x in osoby if x["wiek"]>=minwiek])


@app.route("/api/<string:klucz>/<int:minwiek>")
def minwiekklucz(klucz,minwiek):

    if klucz in klucze:
        return jsonify([x for x in osoby if x["wiek"]>=minwiek])
    else:
        return jsonify({"Error":"Nie jestes uprawniony"})

@app.route("/count")
def count():
    return jsonify({"User": request.remote_addr})


if __name__ == "__main__":
    app.run(debug=True)