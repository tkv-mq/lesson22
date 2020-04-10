from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/list")
def medicines():
    lst = ['Парацетамол', 'Линкас', 'Антигриппин', 'Кавинтон', 'Канефирон']
    return render_template("medicines.html", lst=lst)

@app.route("/recoms")
@app.route("/recoms/<tag>")
def recoms(tag=""):
    return render_template("recoms.html", tag=tag)