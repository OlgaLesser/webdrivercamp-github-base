import requests


def get_repos(some_url):
    response = requests.get(some_url)
    if response.status_code == 200:
        data = response.json()
        print(f"Status Code: {response.status_code}")
        print(f"Total Count: {data['total_count']}")
        items = data['items']
        sorted_items = sorted(items, key=lambda some_item: some_item['full_name'])
        return sorted_items
    else:
        print(f"Error: {response.status_code}")
        return []


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"
    list_of_items = get_repos(url)
    if list_of_items:
        print("\nRepositories (sorted by full_name):")
        for item in list_of_items:
            user = item['owner']['login']
            repo = item['name']
            print(f"{user:15}", repo)
