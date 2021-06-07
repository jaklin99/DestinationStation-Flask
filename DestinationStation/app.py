import pickle

import flask
from flask import Flask
from flask import request
from datetime import datetime
import sklearn
app = Flask(__name__)

with open('model/MLPRegressor.pickle', 'rb') as file:
     model = pickle.load(file)

# /delays?departureStation=ASD&destinationStation=UT&rideTime=2021-06-31T13:59
@app.route('/delays',  methods=['GET'])
def delays():
    departure = request.args.get('departureStation', 'UT')
    destination = request.args.get('destinationStation', 'ASD')
    rideTime = request.args.get(
        'rideTime',
        datetime.now().strftime("%Y-%m-%dT%H:%M")
    )

    return 'Hello World!'


@app.route('/distrubtion',  methods=['GET'])
def distrubtion():

    if flask.request.method == 'POST':
        # get input

        genders_type = flask.request.form['genders_type']
        # marriage status as boolean YES: 1 , NO: 0
        marital_status = flask.request.form['marital_status']
        # Dependents: No. of people dependent on the applicant (0,1,2,3+)
        dependents = flask.request.form['dependents']

        # dependents = dependents_to_int[dependents.upper()]

        # education status as boolean Graduated, Not graduated.
        education_status = flask.request.form['education_status']
        # Self_Employed: If the applicant is self-employed or not (Yes, No)
        self_employment = flask.request.form['self_employment']
        # Applicant Income
        applicantIncome = float(flask.request.form['applicantIncome'])
        # Co-Applicant Income
        coapplicantIncome = float(flask.request.form['coapplicantIncome'])
        # loan amount as integer
        loan_amnt = float(flask.request.form['loan_amnt'])
        # term as integer: from 10 to 365 days...
        term_d = int(flask.request.form['term_d'])
        # credit_history
        credit_history = int(flask.request.form['credit_history'])
        # property are
        property_area = flask.request.form['property_area']
        # property_area = property_area_to_int[property_area.upper()]

        # create original output dict
        output_dict = dict()
        output_dict['Applicant Income'] = applicantIncome
        output_dict['Co-Applicant Income'] = coapplicantIncome
        output_dict['Loan Amount'] = loan_amnt
        output_dict['Loan Amount Term'] = term_d
        output_dict['Credit History'] = credit_history
        output_dict['Gender'] = genders_type
        output_dict['Marital Status'] = marital_status
        output_dict['Education Level'] = education_status
        output_dict['No of Dependents'] = dependents
        output_dict['Self Employment'] = self_employment
        output_dict['Property Area'] = property_area


if __name__ == '__main__':
    app.run()
