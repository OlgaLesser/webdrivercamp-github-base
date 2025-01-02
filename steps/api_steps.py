from behave import *
from base.components.client_api import ClientAPI
from base.components.payload_api import PayloadAPI
from base.components.response_api import ResponseAPI
import json


@step("the API base URL is '{base_url}'")
def set_api_base_url(context, base_url):
    context.api = ClientAPI(base_url)


@step("I send a '{method}' request to '{endpoint}'")
def send_api_request(context, method, endpoint):
    if method.lower() == "get":
        response = context.api.get(endpoint)
    elif method.lower() == "post":
        response = context.api.post(endpoint)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    context.response = response.json()


@step("the response status code is {expected_code}")
def verify_response_status_code(context, expected_code):
    assert context.response.status_code == int(expected_code), f"Unexpected status code: {context.response.status_code}"


@step("the response JSON matches:")
def verify_response_json(context, expected_json):
    expected_data = json.loads(expected_json)
    assert context.response == expected_data, f"Response JSON does not match expectation."


@step("the payload file is '{payload_file}'")
def load_payload(context, payload_file):
    context.payload_api = PayloadAPI(payload_file)
    context.payload = context.payload_api.read_payload()


@step("update payload with '{jsonpath}' to '{value}'")
def update_payload(context, jsonpath, value):
    context.payload_api.update_payload(jsonpath, value)
    context.payload = context.payload_api.read_payload()


@step("the response should have '{jsonpath}' with length '{expected_length}'")
def verify_response_length(context, jsonpath, expected_length):
    response_api = ResponseAPI(context.response)
    response_api.verify_length(jsonpath, int(expected_length))


@step("the response should contain '{jsonpath}' with value '{expected_value}'")
def verify_response_contains(context, jsonpath, expected_value):
    response_api = ResponseAPI(context.response)
    response_api.verify_contains(jsonpath, expected_value)


@step("the response should have '{jsonpath}' equal to '{expected_value}'")
def verify_response_equals(context, jsonpath, expected_value):
    response_api = ResponseAPI(context.response)
    response_api.verify_equals(jsonpath, expected_value)
