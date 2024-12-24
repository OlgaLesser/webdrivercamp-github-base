import requests
from token_service import get_token


def get_with_auth(some_url, some_token):
    some_headers = {"Authorization": f"token {some_token}"}
    response = requests.get(some_url, headers=some_headers)
    if response.status_code == 200:
        data = response.json()
        num_repos = len(data)
        print(f"Status Code: {response.status_code}")
        return num_repos, response.headers
    else:
        print(f"Error: {response.status_code}")
        return 0, {}


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"
    token = get_token()
    num_of_repos, headers = get_with_auth(url, token)
    if num_of_repos > 0:
        print(f"\nTotal Repositories: {num_of_repos}")
        print(f"\nResponse Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")
