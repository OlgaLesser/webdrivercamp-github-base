import requests


class ClientAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error sending GET request to {url}: {e}")

    def post(self, endpoint, headers=None, data=None, json=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if data:
                response = requests.post(url, headers=headers, data=data)
            elif json:
                response = requests.post(url, headers=headers, json=json)
            else:
                raise Exception("Either data or json argument is required for POST requests.")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error sending POST request to {url}: {e}")

    def patch(self, endpoint, headers=None, json=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if not json:
                raise Exception("JSON data is required for PATCH requests.")
            response = requests.patch(url, headers=headers, json=json)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error sending PATCH request to {url}: {e}")

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error sending DELETE request to {url}: {e}")
