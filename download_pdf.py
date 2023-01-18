from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    # TODO how would you improve this code?
    cat_fact = requests.get("https://catfact.ninja/fact").json().get("fact")
    return render_template("index.html", cat_fact=cat_fact)


@app.route("/download_pdf")
def download_pdf():
    # TODO implement a route that downloads the cat fact as a PDF.
    return ""
