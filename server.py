from flask import Flask, render_template, request
from scraping_html import *
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == "POST":
        search_query = request.form["search_query"]
        url = "http://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms={}".format(
            search_query)
        x = search(url)
        # num = 0
        # for businesses in x:
        #     print(x[num])
        #     if num != len(x):
        #         num += 1
        return render_template('test.html', businesses=x)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
