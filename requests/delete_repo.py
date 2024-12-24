import requests
from token_service import get_token


def delete_repo(url, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Status Code: {response.status_code} (No Content)")
        print("Repository deleted successfully!")
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
    return response.status_code


if __name__ == "__main__":
    my_url = "https://api.github.com/repos/{}/{}"
    my_token = get_token()
    owner = "OlgaLesser"
    repo = "repo-created-with-api"
    formatted_url = my_url.format(owner, repo)
    status_code = delete_repo(formatted_url, my_token)
    if status_code not in [204, 404]:
        print(f"An unexpected error occurred (status code: {status_code})")
