from flask import Flask, request, jsonify
import random
import uuid

class SimulatedExchange:
    def __init__(self):
        self.users = {}  # Stores user data indexed by API key

    def register_user(self, initial_cash):
        api_key = str(uuid.uuid4())  # Generate a unique API key
        self.users[api_key] = {"cash": initial_cash, "asset": 0}
        return api_key

    def get_random_price(self):
        return random.uniform(5, 15)  # Random price between 5 and 15

    def buy(self, api_key, amount):
        user = self.users.get(api_key)
        if not user:
            return 'Invalid API key'

        price = self.get_random_price()
        cost = amount * price
        if cost <= user["cash"]:
            user["cash"] -= cost
            user["asset"] += amount
            return f'Bought {amount} assets for {cost} cash at price {price}.'
        else:
            return 'Not enough cash to buy.'

    def sell(self, api_key, amount):
        user = self.users.get(api_key)
        if not user:
            return 'Invalid API key'

        price = self.get_random_price()
        if amount <= user["asset"]:
            user["asset"] -= amount
            revenue = amount * price
            user["cash"] += revenue
            return f'Sold {amount} assets for {revenue} cash at price {price}.'
        else:
            return 'Not enough assets to sell.'

    def get_balance(self, api_key):
        user = self.users.get(api_key)
        if not user:
            return 'Invalid API key'
        return user

    def get_price(self):
        return {'price': self.get_random_price()}

app = Flask(__name__)
exchange = SimulatedExchange()

@app.route('/register', methods=['POST'])
def register_user():
    initial_cash = request.json.get('initial_cash', 1000)  # Default initial cash is 1000
    api_key = exchange.register_user(initial_cash)
    return jsonify({'api_key': api_key})

@app.route('/buy', methods=['POST'])
def buy():
    api_key = request.json.get('api_key')
    amount = request.json.get('amount')
    return jsonify({'response': exchange.buy(api_key, amount)})

@app.route('/sell', methods=['POST'])
def sell():
    api_key = request.json.get('api_key')
    amount = request.json.get('amount')
    return jsonify({'response': exchange.sell(api_key, amount)})

@app.route('/balance', methods=['GET'])
def balance():
    api_key = request.args.get('api_key')
    return jsonify(exchange.get_balance(api_key))

@app.route('/price', methods=['GET'])
def price():
    return jsonify(exchange.get_price())

if __name__ == '__main__':
    app.run(debug=True)
