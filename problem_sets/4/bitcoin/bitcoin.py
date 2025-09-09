import requests
import sys


def parse_arguments():
    """ Parses and validate the command-line arguments """

    if len(sys.argv) != 2:
        sys.exit("Error: Missing command-line argument <number_of_bitcoins>")

    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Bitcoin amount must be a valid number")

    if bitcoin_amount <= 0:
        sys.exit("Error: Bitcoin amount cannot be negative or zero")
    
    return bitcoin_amount

def get_bitcoin_price(api_key):
    """ Fetches the current Bitcoin price data from the CoinCap API """

    url = "rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        # Fetches Bitcoin data from the API
        res = requests.get(url)
        res.raise_for_status()      # Raise exception for HTTP errors
        
        # Parse JSON response and extract the price
        data = res.json()
        bitcoin_price = float(data["data"]["priceUsd"])
        
        return bitcoin_price
    
    # Handles API communinications and error cases """
    except (KeyError, ValueError):
        sys.exit("Error: Failed to parse API response.")
    except requests.exceptions.ConnectionError:
        sys.exit("Error: Network connection failed. Please check your internet connection.")
    except requests.exceptions.HTTPError as e:
        if e.res.status_code == 401:
            sys.exit("Error: Invalid API key. Please check your CoinCap API key.")
        elif e.res.status_code == 404:
            sys.exit("Error: API request not found.")
        else:
            sys.exit(f"Error: API request failed with status code {e.res.status_code}.")
    except reqeusts.exceptions.RequestException:
        sys.exit("Error: Unable to connect to CoinCap API")


def main():
    """ Main function calculates the cost of buying Bitcoins and format the amount to the specified currency string"""
    
    # Parse and validate command-line argument count
    n = parse_arguments()

    # API configuration 
    API_KEY = "1554b9a3636d57f96a6a68cfcb607e282e045ebe39d6ca84ba15d2883d997194"

    # Get the current Bitcoin price and calculate the cost
    price = get_bitcoin_price(API_KEY)
    total_cost = n * price

    # Format and display result
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
