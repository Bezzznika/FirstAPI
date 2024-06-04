from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra
    return jsonify(user_data),200

@app.route('/get_currency_rate')
def get_currency_rate():
    currency_rate = {
        'USDtoSUM': 12614,
        'EURtoSUM': 13668,
        'RUBtoSUM': 141
    }
    return jsonify(currency_rate),200



@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()

    return jsonify(data),201

if __name__ == "__main__":
    app.run(debug=True)
