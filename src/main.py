from flask import Flask, request, render_template
from scraper import scrape_zone
import string

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():
    region = request.form['text']
    scrapedata = scrape_zone(region)
    context = dict(region=scrapedata["region"], color=scrapedata["color"])
    return render_template("index.html", **context)
