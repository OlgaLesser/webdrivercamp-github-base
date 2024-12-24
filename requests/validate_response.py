import json
import requests
from pprint import pprint


def find_mismatched_data(url, filename):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: Failed to retrieve data from SWAPI (status code: {response.status_code})")
            return None
        swapi_data = response.json()["results"]
        with open(filename, "r") as file:
            expected_data = json.load(file)
        mismatches = {}
        for swapi_planet, expected_planet in zip(swapi_data, expected_data["results"]):
            if len(swapi_planet) != len(expected_planet):
                print(f"Mismatch: Length of the planet object differ between SWAPI and file.")
                return None
            planet_name = swapi_planet["name"]
            mismatches[planet_name] = {}
            for key, expected_value in expected_planet.items():
                actual_value = swapi_planet.get(key)
                if actual_value != expected_value:
                    mismatches[planet_name][key] = {"Expected": expected_value, "Actual": actual_value}
        return mismatches
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    my_url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"
    my_mismatches = find_mismatched_data(my_url, file_name)
    if my_mismatches:
        pprint(my_mismatches)
    else:
        print("No mismatches found!")
