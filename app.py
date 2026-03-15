#!/usr/bin/env python3
"""
ChiroAutomationApp - Automation for filling in a referral
"""

import os
import sys
from pathlib import Path
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def process_referral(patient_data):
    """Process the referral automation logic"""
    # TODO: Add your automation logic here
    # For example:
    # - Fill out referral forms
    # - Process patient data
    # - Generate documents
    
    firstName = patient_data.get('firstName', 'Unknown')
    lastName = patient_data.get('lastName', 'Patient')
    fullName = f"{firstName} {lastName}"
    
    result = {
        "status": "success",
        "message": f"Referral processed for {fullName}",
        "patient_id": patient_data.get('patientId', 'N/A'),
        "referral_type": patient_data.get('referralType', 'N/A')
    }
    return result

@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """Process referral form"""
    patient_data = {
        'firstName': request.form.get('firstName'),
        'lastName': request.form.get('lastName'),
        'patientId': request.form.get('patientId'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'referralType': request.form.get('referralType'),
        'notes': request.form.get('notes')
    }
    
    result = process_referral(patient_data)
    return jsonify(result)

def main():
    """Main function for running the automation app"""
    print("ChiroAutomationApp starting...")
    print("Access the web interface at: http://localhost:8080")
    app.run(debug=True, host='0.0.0.0', port=8080)

if __name__ == "__main__":
    main()
