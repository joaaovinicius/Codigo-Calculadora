from flask import Flask, request, jsonify
from calculator import calculate

app = Flask(__name__)

@app.route("/calc", methods=["POST"])
def calc_route():
    data = request.json
    a = data["a"]
    b = data["b"]
    op = data["op"]

    try:
        result = calculate(a, b, op)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(port=5000)
