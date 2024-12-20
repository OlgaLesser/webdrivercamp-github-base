import json
from jsonpath_ng import parse, exceptions as jsonpath_ng_exceptions


class PayloadAPI:
    def __init__(self, payload_file):
        with open(payload_file, 'r') as f:
            self.payload = json.load(f)

    def read_payload(self):
        return self.payload

    def update_payload(self, jsonpath, value):
        try:
            expr = parse(jsonpath)
            matches = expr.find(self.payload)
            if not matches:
                raise ValueError(f"JSONPath expression '{jsonpath}' did not match any key in the payload.")
            for match in matches:
                match.set(value)
        except jsonpath_ng_exceptions.JSONPathError as e:
            raise ValueError(f"Invalid JSONPath expression: {e}")

    def replace_value(self, key, new_value):
        self.update_payload(f"$." + key, new_value)

    def add_key_value(self, key, value):
        self.payload[key] = value

    def delete_key(self, key):
        del self.payload[key]
