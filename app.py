from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("displaydata.html", data="Hi there")

@app.route('/read-data')
def read_data():
    f = open("datafile", "r")
    return render_template("displaydata.html", data=f.read())

@app.route('/endpoint', methods = ['POST'])
def endpoint_post():
    data_rec=request.get_data().decode("utf-8")
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', data_rec)
    f = open('datafile', 'a')
    f.write(data_rec + ' -- ')
    f.close()
    return render_template("displaydata.html", data="success")

@app.route('/wipe')
def wipe_file():
    f = open('datafile', 'w').close()
    return render_template("displaydata.html", data="success")
