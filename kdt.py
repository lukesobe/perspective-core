from perspective_core import app  # Inherit from core

@app.route('/api/kdt', methods=['GET'])
def kdt_endpoint():
    return jsonify({"kdt": "Active"})