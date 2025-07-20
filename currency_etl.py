import requests

def fetch_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    
    print("Base Currency:", data["base"])
    print("Rates:", data["rates"])

if __name__ == "__main__":
    fetch_exchange_rates()


