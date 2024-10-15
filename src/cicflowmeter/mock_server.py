from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"status": "success", "message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run(port=8000)
