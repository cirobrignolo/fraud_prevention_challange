import requests

def get_usd_conversion(amount, currency):
    try:
        response = requests.get("https://currencyconverter.p.rapidapi.com/", params={
            "from_amount": amount,
            "from": currency,
            "to": "USD",
        })
        response.raise_for_status()
        data = response.json()
        return data.get('converted_amount', amount)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Returns the original amount if there was an error (only in this case, because the API may not be functioning)
    return amount
