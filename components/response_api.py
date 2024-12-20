import jsonpath_rw_ext as jp


class ResponseAPI:
    def __init__(self, response_json):
        self.data = response_json

    def verify_length(self, jsonpath, expected_length):
        parsed = jp.parse(self.data)
        result = parsed.search(jsonpath)
        actual_length = len(result)
        assert actual_length == expected_length, (f"JSONPath '{jsonpath}' length mismatch: Expected {expected_length}, "
                                                  f"Actual {actual_length}")

    def verify_contains(self, jsonpath, expected_value):
        parsed = jp.parse(self.data)
        result = parsed.search(jsonpath)
        assert any(expected_value in str(item) for item in result), (f"JSONPath '{jsonpath}' value not found: Expected "
                                                                     f"to contain '{expected_value}'")

    def verify_equals(self, jsonpath, expected_value):
        parsed = jp.parse(self.data)
        result = parsed.search(jsonpath)
        assert result[0] == expected_value, f"JSONPath '{jsonpath}' value mismatch: Expected {expected_value}, Actual {result[0]}"