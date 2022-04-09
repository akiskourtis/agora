import requests
import flask
from flask import Flask, request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    #bid_req = json.loads(request.data)

    bid_id = request.args.get('bid_id')
    app_id = request.args.get('app_id')
    app_name = request.args.get('app_name')
    dev_id = request.args.get('dev_id')
    dev_os = request.args.get('dev_os')
    dev_long = request.args.get('dev_long')
    dev_lat = request.args.get('dev_lat')
    dev_country = request.args.get('dev_country')
    #print(dev_country)
    params = {"dev_long": dev_long, "dev_lat": dev_lat,"dev_country": dev_country}
    camp_req = requests.get(url="http://127.0.0.1:5001/", params=params)
    #print(camp_req.json())
    return jsonify(camp_req.json())

app.run(host='0.0.0.0', port=5000,debug=True)
