#!/usr/bin/env python3
"""
Apple (AAPL) Stock Tracker
This script tracks Apple stock price and provides basic analysis.
"""

import requests
import json
from datetime import datetime

def get_aapl_price():
    """
    Fetch current AAPL stock price from a financial API
    """
    try:
        # Using Alpha Vantage API (replace with your API key)
        api_key = "YOUR_API_KEY_HERE"
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey={api_key}"
        
        response = requests.get(url)
        data = response.json()
        
        if "Global Quote" in data:
            quote = data["Global Quote"]
            price = float(quote["05. price"])
            change = float(quote["09. change"])
            change_percent = quote["10. change percent"].rstrip('%')
            
            return {
                "symbol": "AAPL",
                "price": price,
                "change": change,
                "change_percent": change_percent,
                "timestamp": datetime.now().isoformat()
            }
        else:
            print("Error: Unable to fetch stock data")
            return None
            
    except Exception as e:
        print(f"Error fetching AAPL price: {e}")
        return None

def display_stock_info(stock_data):
    """
    Display formatted stock information
    """
    if stock_data:
        print(f"\n=== {stock_data['symbol']} Stock Information ===")
        print(f"Current Price: ${stock_data['price']:.2f}")
        print(f"Change: ${stock_data['change']:.2f} ({stock_data['change_percent']}%)")
        print(f"Last Updated: {stock_data['timestamp']}")
        print("=" * 40)
    else:
        print("No stock data available")

def save_to_file(stock_data, filename="aapl_data.json"):
    """
    Save stock data to a JSON file
    """
    try:
        with open(filename, 'w') as f:
            json.dump(stock_data, f, indent=2)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    """
    Main function to run the AAPL tracker
    """
    print("AAPL Stock Tracker")
    print("-" * 20)
    
    # Fetch stock data
    stock_data = get_aapl_price()
    
    # Display information
    display_stock_info(stock_data)
    
    # Save data if available
    if stock_data:
        save_to_file(stock_data)

if __name__ == "__main__":
    main()
