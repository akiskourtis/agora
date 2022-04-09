#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from random_word import RandomWords
import random
import string
import helper

r = RandomWords()
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'campaigns',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class Campaign(db.Document):
    cid = db.IntField()
    name = db.StringField()
    price = db.IntField()
    java = db.StringField()
    countries = db.ListField()
    coord = db.ListField()
    def to_json(self):
        return {"cid": self.cid,
                "name": self.name,
                "price" : self.price,
                "java" : self.java,
                "countries" : self.countries,
                "coord" : self.coord }

@app.route('/', methods=['GET'])
def query_records():
    dev_long = request.args.get("dev_long")
    dev_lat = request.args.get("dev_lat")
    dev_country = request.args.get("dev_country")
    #print(dev_lat)
    #print(dev_country)

    campaigns = Campaign.objects(countries__icontains=dev_country)
    campaign = campaigns.order_by('-price').first()
    #print(campaign["price"])

    if not campaign:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify({'country': dev_country, 'price': campaign["price"]})


@app.route('/random_loc', methods=['GET'])
def random_loc():
    #num = request.json.get("num")

    #campaigns = db.campaigns.aggregate([{'$sample': {'size': 1}}])
    campaigns = Campaign.objects.aggregate([{'$sample': {'size': 1}}])
    list_data = (list(campaigns)[0])
    rand_coord = list_data["coord"][0]
    json_d = json.loads(str(rand_coord))
    #print(json_d)
    if not campaigns:
        return jsonify({'error': 'data not found'})
    else:

        return jsonify(json_d)

@app.route('/', methods=['PUT'])
def create_record():
    #record = json.loads(request.data)
    letters = string.ascii_letters
    for x in range(50):
        #print(x)
        campaign = Campaign(cid = random.randint(1,1000),
                    name = r.get_random_word(),
                    price = random.randint(1,100),
                    java = ''.join(random.choice(letters) for i in range(20)),
                    countries = helper.random_countries(random.randint(1,3)),
                    coord = helper.random_coords(random.randint(1,5))).save()
    return jsonify("added 50 items")



@app.route('/all', methods=['DELETE'])
def delete_all():
    Campaign.objects.delete()
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001,debug=True)