from flask import Flask
import flask
import opencorp
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/opencorp")
def search_oc():
    return flask.jsonify({ 'a': 1, 'b': 3})

if __name__ == "__main__":
    app.run()

url = 'https://uksanctionslist.apispark.net:443/v1/entities?Organization_list=...'
