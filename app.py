from flask import Flask
import flask
import opencorp
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
    print 'foo'
    return "Hello World!"

@app.route("/opencorp")
def search_oc():
    name = flask.request.args.get('q')
    print name
    companies = opencorp.fetch_companies(name)
    return flask.jsonify(companies)

if __name__ == "__main__":
    app.run()

url = 'https://uksanctionslist.apispark.net:443/v1/entities?Organization_list=...'
