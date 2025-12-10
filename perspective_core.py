# Perspective Core Platform
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/verticals', methods=['GET'])
def get_verticals():
    return jsonify({"verticals": ["orthodox-perspective", "kdt"]})

@app.route('/api/onboard', methods=['POST'])
def onboard_vertical():
    data = request.json
    vertical = data.get('vertical')
    # Logic to onboard new vertical
    return jsonify({"status": "onboarded", "vertical": vertical})

if __name__ == '__main__':
    app.run(debug=True)