import pymongo
from flask import Flask, request, jsonify
from bson.json_util import dumps
from flask_restx import Resource, Api

client = pymongo.MongoClient('mongodb+srv://phihd:iXkIXCNJhQNQriwF@cluster0.vwz1m.mongodb.net/bdp-a1?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
database = client['bdp-a1']
covid_table = database['covid19']
covid_tables = [database['covid19'], database['covid19_1'], database['covid19_2']]

app = Flask(__name__)
api = Api(app)
covid_api = api.namespace('apps')

@app.route('/ingestion', methods=['POST'])
def post():
	covid_table.insert_many(request.json)
	return ''

@app.route('/clear', methods=['POST'])
def clear():
	for _covid_table in covid_tables:
		_covid_table.delete_many(request.json)
	return ''

@covid_api.route('/find/date=<date>&country=<country>', methods=['GET'])
class find(Resource):
	def get(self, date, country):
		covid_table.create_index(['dateRep','countriesAndTerritories'])
		formatted_date = date.replace("-", "/")
		result = list(covid_table.find({'dateRep':formatted_date, 'countriesAndTerritories':country}))
		return dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
