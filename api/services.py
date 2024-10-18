import logging
import requests

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def get_usd_conversion(amount, currency):
    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"
    
    headers = {
        "x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com",
        "x-rapidapi-key": "821945cee4mshfb3769699c79de2p17d012jsnfde78438b77e"
    }

    params = {
        "amount": amount,
        "from": currency,
        "to": "USD"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if not data.get('success'):
            error_info = data.get('error', {})
            error_code = error_info.get('code')
            error_type = error_info.get('type')
            error_message = error_info.get('info')

            full_error_msg = (f"API Error: {error_type} (Code: {error_code}) - {error_message}")
            logging.error(full_error_msg)
            raise ValueError(full_error_msg)

        return data.get('result', amount)

    except requests.exceptions.HTTPError as http_err:
        error_msg = f"HTTP error occurred: {http_err}"
        logging.error(error_msg)
        raise http_err

    except requests.exceptions.RequestException as req_err:
        error_msg = f"Request error occurred: {req_err}"
        logging.error(error_msg)
        raise req_err

    except Exception as e:
        error_msg = f"An unexpected error occurred: {e}"
        logging.error(error_msg)
        raise e
