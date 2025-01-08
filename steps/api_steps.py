from behave import *
from base.components.client_api import ClientAPI
from base.components.payload_api import PayloadAPI
from base.components.response_api import ResponseAPI
from token_service import get_token


@step("the API base URL is '{base_url}'")
def set_api_base_url(context, base_url):
    context.api = ClientAPI(base_url)


@step("I send a '{method}' request to '{endpoint}'")
def send_api_request(context, method, endpoint):
    if method.lower() == "get":
        response = context.api.get(endpoint)
    elif method.lower() == "post":
        response = context.api.post(endpoint, json=context.payload)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    context.response = response


@step("I have a valid access token")
def have_valid_access_token(context):
    context.access_token = get_token()


@step("I send a '{method}' request with authentication to '{endpoint}'")
def send_authenticated_request(context, method, endpoint):
    if not hasattr(context, 'access_token'):
        raise Exception("Access token not found in context. Please define it in a previous step.")
    headers = {"Authorization": f"token {context.access_token}"}
    if method.lower() not in ("get", "post", "patch", "delete"):
        raise ValueError(f"Unsupported HTTP method: {method}")
    if method.lower() == "get":
        response = context.api.get(endpoint, headers=headers)
    elif method.lower() == "post":
        if not hasattr(context, 'payload'):
            raise Exception("Payload required for POST requests.")
        response = context.api.post(endpoint, headers=headers, json=context.payload)
    elif method.lower() == "patch":
        if not hasattr(context, 'payload'):
            raise Exception("Payload required for PATCH requests.")
        response = context.api.patch(endpoint, headers=headers, json=context.payload)
    elif method.lower() == "delete":
        response = context.api.delete(endpoint, headers=headers)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    context.response = response


@step("the response status code is {expected_code}")
def verify_response_status_code(context, expected_code):
    assert context.response.status_code == int(expected_code), f"Unexpected status code: {context.response.status_code}"


@step("the request body is '{payload_file}'")
def load_payload(context, payload_file):
    context.payload_api = PayloadAPI(f"base/data/payloads/{payload_file}.json")
    context.payload = context.payload_api.read_payload()


@step("update payload with '{jsonpath}' to '{value}'")
def update_payload(context, jsonpath, value):
    context.payload_api.update_payload(jsonpath, value)
    context.payload = context.payload_api.read_payload()


@step("the response should have '{jsonpath}' with length '{expected_length}'")
def verify_response_length(context, jsonpath, expected_length):
    response_api = ResponseAPI(context.response)
    response_api.verify_length(jsonpath, int(expected_length))


@step("the response should have '{jsonpath}' with length greater than 0")
def verify_response_length_greater_than_zero(context, jsonpath):
    response_api = ResponseAPI(context.response)
    result = response_api.get_values_by_jsonpath(jsonpath)
    assert len(str(result)) > 0, f"Expected length of '{jsonpath}' to be greater than 0, but found {len(str(result))}"


@step("the response should contain '{jsonpath}' with value '{expected_value}'")
def verify_response_contains(context, jsonpath, expected_value):
    response_api = ResponseAPI(context.response)
    response_api.verify_contains(jsonpath, expected_value)


@step("the response should have '{jsonpath}' equal to '{expected_value}'")
def verify_response_equals(context, jsonpath, expected_value):
    response_api = ResponseAPI(context.response)
    response_api.verify_equals(jsonpath, expected_value)


@step("the response should contain items")
def verify_response_count(context):
    response_api = ResponseAPI(context.response)
    result = response_api.get_items_count()
    assert result > 0, f"Expected count to be greater than 0"


@step('a repository named "{repo_name}" has been created')
def repository_created(context, repo_name):
    context.created_repository_name = repo_name
