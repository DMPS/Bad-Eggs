from flask import Flask
import flask
import opencorp
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/opencorp")
def search_oc():
    name = flask.request.args.get('q')
    companies = opencorp.fetch_companies(name)
    ret_obj = { 'result': map(process_company, companies) }
    return flask.jsonify(ret_obj)

@app.route("/sanctions")
def search_sanctions():
    name = flask.request.args.get('q')
    sanctions = opencorp.fetch_sanctions(name)
    return sanctions

def process_company(co):
    susp = opencorp.suspicious(co)
    return { 'name': co['company']['name'], 'suspicious': susp }

if __name__ == "__main__":
    app.run()

