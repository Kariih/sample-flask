from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/my_data/', methods=['POST'])
def work_with_data():
    print request.form

@app.route('/<user>')
def user(user):
    return render_template("displaydata.html", data=user)
