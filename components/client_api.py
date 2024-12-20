import requests


class ClientAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error sending GET request to {url}: {e}")

    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if data:
                response = requests.post(url, data=data)
            elif json:
                response = requests.post(url, json=json)
            else:
                raise Exception("Either data or json argument is required for POST requests.")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error sending POST request to {url}: {e}")
