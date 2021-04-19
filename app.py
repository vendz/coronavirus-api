import requests
from flask import Flask, jsonify
import covid

app = Flask(__name__)


@app.route('/covid/<country>', methods=['GET'])
def findInfo(country):
    try:
        return jsonify({"Total Cases": covid.information(country)[0].replace(",", ""),
                        "Total Deaths": covid.information(country)[1].replace(",", ""),
                        "Total Recovered": covid.information(country)[2].replace(",", ""),
                        "Closed Cases": covid.information(country)[3].replace(",", ""),
                        "active Cases": covid.information(country)[4]})
    except requests.exceptions.RequestException as e:
        return jsonify({"No Entries Found": str(e)})


@app.route('/covid/countries')
def all_countries():
    try:
        return jsonify({"All Countries": covid.all_countries()})
    except requests.exceptions.RequestException as e:
        return jsonify({"No Entries Found": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
