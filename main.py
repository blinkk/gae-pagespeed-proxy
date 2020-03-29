import flask
import json
import requests

app = flask.Flask(__name__)

API_KEY = os.environ['PAGESPEED_API_KEY']
URL = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={key}&strategy={strategy}'

@app.route('/')
def run():
    url = flask.request.args.get('url')
    strategy = flask.request.args.get('strategy') or 'desktop'
    api_url = URL.format(url=url, key=API_KEY, strategy=strategy)
    resp = requests.get(api_url)
    resp_json = resp.json()
    results = []
    if 'lighthouseResult' not in resp_json:
        data = resp_json
        return flask.jsonify(data)
    for key, vals in resp_json['lighthouseResult']['audits'].items():
        vals.pop('details', None)
        results.append(vals)
    data = {'audits': results}
    resp = flask.make_response(flask.jsonify(data))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
