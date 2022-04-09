#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from random_word import RandomWords
import random
import string
import countries_list

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
    countries = db.StringField()
    coord = db.StringField()
    def to_json(self):
        return {"cid": self.cid,
                "name": self.name,
                "price" : self.price,
                "java" : self.java,
                "countries" : self.countries,
                "coord" : self.coord }

@app.route('/', methods=['GET'])
def query_records():
    cid = request.args.get('cid')
    campaign = Campaign.objects(cid=cid).first()
    if not campaign:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(campaign.to_json())

@app.route('/', methods=['PUT'])
def create_record():
    #record = json.loads(request.data)
    letters = string.ascii_letters
    for x in range(10):
        campaign = Campaign(cid = random.randint(1,100),
                    name = r.get_random_word(),
                    price = random.randint(1,100),
                    java = ''.join(random.choice(letters) for i in range(20)),
                    countries = str(countries_list.countries_arr[random.randint(1,100)]),
                    coord = str([(random.random()*2.0, random.random()*2.0) for _ in range (10)])).save()
    return jsonify("added 100 items")

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001,debug=True)