import requests

# Base URL of the Flask server
base_url = "http://127.0.0.1:5000"

# 1. Register a new user
register_response = requests.post(f"{base_url}/register", json={"initial_cash": 1000})
api_key = register_response.json()['api_key']
print("Registered new user with API Key:", api_key)

# 2. Get the current price of the asset
price_response = requests.get(f"{base_url}/price")
price = price_response.json()['price']
print("Current asset price:", price)

# 3. Get the user's balance
balance_response = requests.get(f"{base_url}/balance", params={"api_key": api_key})
balance = balance_response.json()
print("User balance:", balance)

# 4. Buy some amount of the asset
buy_response = requests.post(f"{base_url}/buy", json={"api_key": api_key, "amount": 10})
print("Buy response:", buy_response.json())

# 5. Sell some amount of the asset
sell_response = requests.post(f"{base_url}/sell", json={"api_key": api_key, "amount": 5})
print("Sell response:", sell_response.json())

# Get the user's balance again to see the changes
new_balance_response = requests.get(f"{base_url}/balance", params={"api_key": api_key})
new_balance = new_balance_response.json()
print("New user balance:", new_balance)
