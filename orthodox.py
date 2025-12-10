from perspective_core import app  # Inherit

@app.route('/api/orthodox', methods=['GET'])
def orthodox_endpoint():
    return jsonify({"orthodox": "Perspective active"})