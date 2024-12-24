import requests
from token_service import get_token


def get_created_repo(url, token, owner, repo):
    headers = {"Authorization": f"token {token}"}
    formatted_url = url.format(owner=owner, repo=repo)
    response = requests.get(formatted_url, headers=headers)
    if response.status_code == 200:
        print(f"Status Code: {response.status_code} (OK)")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None


def validate_repo_details(repo, expected_name, expected_private, expected_has_wiki, expected_owner_login):
    assert repo['name'] == expected_name, f"Name mismatch: expected '{expected_name}', got '{repo['name']}"
    assert repo['private'] == expected_private, f"Private flag mismatch: expected {expected_private},"f"got {repo['private']}"
    assert repo['has_wiki'] == expected_has_wiki, f"has_wiki flag mismatch: expected {expected_has_wiki},"f"got {repo['has_wiki']}"
    assert repo['owner']['login'] == expected_owner_login, f"Owner mismatch: expected '{expected_owner_login}',"f"got '{repo['owner']['login']}"
    print("All validation checks passed!")


if __name__ == "__main__":
    my_url = "https://api.github.com/repos/{owner}/{repo}"
    my_token = get_token()
    my_owner = "OlgaLesser"
    my_repo = "repo-created-with-api"
    my_response = get_created_repo(my_url, my_token, my_owner, my_repo)
    if my_response:
        validate_repo_details(my_response, my_repo, True, False, my_owner)
