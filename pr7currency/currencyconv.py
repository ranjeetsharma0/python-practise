from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_qYL0Z6f7jIxkSj4Gsir2dpkJNLA7ARSdQxHqf2zb"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data1 = get(url).json()['data']

    data1 = list(data1.items())
    data1.sort()
    
    return data1


def print_currencies(currencies):
    for currency, rate in currencies:
        print(f"INITIALS: {currency}, RATE = {rate}")


def exchange_rate(currency1, currency2):
    endpoint = f"v1/latest?apikey={API_KEY}&currencies={currency1}%2C{currency2}"
    url = BASE_URL + endpoint
    data = get(url).json()['data']
    if len(data) == 0:
        print("invalid currency")
        return
    
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate} " )

    """ rate1 = data.get(currency1)
    rate2 = data.get(currency2)

    if rate1 and rate2:
        exchange_rate_value = rate2 / rate1
        print(f"The exchange rate from {currency1} to {currency2} is: {exchange_rate_value}")
    else:
        print(f"Error: Could not retrieve exchange rates for {currency1} and/or {currency2}.")

 """
exchange_rate("INR", "JPY")