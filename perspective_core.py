# Perspective Core Platform
import os
from flask import Flask, request, jsonify
from mandate_sentinel import check_mandate
from blackhorse_hawk import hawk_scan

app = Flask(__name__)

@app.route('/api/verticals', methods=['GET'])
def get_verticals():
    return jsonify({"verticals": ["orthodox-perspective", "kdt"]})

@app.route('/api/onboard', methods=['POST'])
def onboard_vertical():
    data = request.json
    vertical = data.get('vertical')
    # Logic to onboard new vertical
    compliance = {'legal': True}  # Example
    mandate_status = check_mandate(compliance)
    scan_data = {'scan': True}  # Example
    hawk_status = hawk_scan(scan_data)
    return jsonify({"status": "onboarded", "vertical": vertical, "mandate": mandate_status, "hawk": hawk_status})

if __name__ == '__main__':
    app.run(debug=True)