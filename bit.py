import time
import requests
from datetime import datetime

# CoinGecko API
URL = "https://api.coingecko.com/api/v3/coins/markets"

# Cryptocurrency list
COINS = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "solana": "SOL",
    "cardano": "ADA",
    "ripple": "XRP"
}

# Currency
CURRENCY = "usd"


def fetch_crypto_prices():
    """Fetch current price, 24h change, high and low prices."""

    params = {
        "vs_currency": CURRENCY,
        "ids": ",".join(COINS.keys()),
        "price_change_percentage": "24h"
    }

    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error fetching cryptocurrency data:", e)
        return []


def display_prices(prices):
    """Display cryptocurrency prices."""

    print("\n--- Update Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "---")

    for coin in prices:

        coin_id = coin["id"]
        symbol = COINS.get(coin_id, coin_id.upper())

        price = coin.get("current_price", 0)
        change = coin.get("price_change_percentage_24h", 0)
        high = coin.get("high_24h", 0)
        low = coin.get("low_24h", 0)

        print(
            f"{symbol}: "
            f"${price:,.2f} | "
            f"24h Change: {change:.2f}% | "
            f"High: ${high:,.2f} | "
            f"Low: ${low:,.2f}"
        )


# Main program
print("==========================================")
print("     CRYPTOCURRENCY PRICE TRACKER")
print("==========================================")

while True:

    prices = fetch_crypto_prices()

    if prices:
        display_prices(prices)
    else:
        print("Unable to fetch cryptocurrency prices.")

    print("\nUpdating again after 60 seconds...")
    time.sleep(60)