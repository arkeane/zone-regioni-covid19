from flask import Flask, request, render_template
from scraper import scrape_zone
import string
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():
    region = request.form['text'].lower()
    color = scrape_zone(region)
    region = string.capwords(region)
    context = dict(region=region, color=color)
    return render_template("index.html", **context)


if __name__ == '__main__':
    app.run(debug=True)
