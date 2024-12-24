import requests
from token_service import get_token


def update_repo(url, token, description):
    headers = {"Authorization": f"token {token}"}
    data = {"description": description}
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Status Code: {response.status_code} (OK)")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None


if __name__ == '__main__':
    my_url = "https://api.github.com/repos/{}/{}"
    my_token = get_token()
    owner = "OlgaLesser"
    repo = "repo-created-with-api"
    my_description = "I know Python Requests!"
    my_response = update_repo(my_url.format(owner, repo), my_token, my_description)
    if my_response:
        assert my_response['description'] == my_description, f"Description update failed."
        print("Description updated successfully!")
