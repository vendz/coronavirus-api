import requests
from flask import Flask, jsonify
import covid

app = Flask(__name__)


@app.route('/')
def index():
    return "API is UP and running"


@app.route('/covid/', methods=['GET', 'POST'])  # world-wide stats
def global_results():
    try:
        return jsonify({"Total Cases": covid.global_info()[0],
                        "Total Deaths": covid.global_info()[1],
                        "Total Recovered": covid.global_info()[2],
                        "active Cases": covid.global_info()[3],
                        "Closed Cases": covid.global_info()[4]})
    except requests.exceptions.RequestException as e:
        return jsonify({"No Entries Found": str(e)})


@app.route('/covid/<country>', methods=['GET', 'POST'])     # country-wise stats
def findInfo(country):
    try:
        return jsonify({"Total Cases": covid.information(country)[0],
                        "Total Deaths": covid.information(country)[1],
                        "Total Recovered": covid.information(country)[2],
                        "Closed Cases": covid.information(country)[3],
                        "active Cases": covid.information(country)[4]})
    except requests.exceptions.RequestException as e:
        return jsonify({"No Entries Found": str(e)})
    except IndexError as e:
        return jsonify({"Error": str(e)})


@app.route('/covid/countries', methods=['GET', 'POST'])     # list of all countries
def all_countries():
    try:
        return jsonify({"All Countries": covid.all_countries()})
    except requests.exceptions.RequestException as e:
        return jsonify({"No Entries Found": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
