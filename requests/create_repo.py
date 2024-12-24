import requests
from pprint import pprint
from token_service import get_token


def create_repo(some_url, some_token, some_name, private=True, has_wiki=False):
    headers = {"Authorization": f"token {some_token}"}
    data = {"name": some_name, "private": private, "has_wiki": has_wiki}
    response = requests.post(some_url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Status Code: {response.status_code} (Created)")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None


if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'
    token = get_token()
    name = "repo-created-with-api"
    try:
        repo = create_repo(url, token, name)
        if repo:
            pprint(repo)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
