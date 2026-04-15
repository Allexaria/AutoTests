import pytest


def parse_json(response, context):
    try:
        return response.json()
    except ValueError:
        pytest.fail(f"{context}: ответ не JSON. Текст: {response.text}")


def assert_status_code(response, expected, context):
    assert (
        response.status_code == expected
    ), f"{context}: ожидали HTTP {expected}, получили {response.status_code}"


def assert_response_code(data, expected, context):
    assert (
        data.get("responseCode") == expected
    ), f"{context}: ожидали responseCode {expected}, получили {data.get('responseCode')}"


def assert_response_code_as_str(data, expected, context):
    assert str(data.get("responseCode")) == str(
        expected
    ), f"{context}: ожидали responseCode {expected}, получили {data.get('responseCode')}"


def assert_message_contains(data, expected_substring, context):
    message = data.get("message", "").lower()
    assert (
        expected_substring.lower() in message
    ), f"{context}: ожидали '{expected_substring}', получили: {data.get('message')}"


def assert_has_list_key(data, key, context):
    assert key in data, f"{context}: ключ '{key}' отсутствует"
    assert isinstance(data[key], list), f"{context}: '{key}' должен быть списком"


def assert_has_dict_key(data, key, context):
    assert key in data, f"{context}: ключ '{key}' отсутствует"
    assert isinstance(data[key], dict), f"{context}: '{key}' должен быть словарем"


def assert_status_or_text_contains(response, expected_status, expected_text, context):
    assert (
        response.status_code == expected_status or expected_text.lower() in response.text.lower()
    ), (
        f"{context}: ожидали HTTP {expected_status} или текст '{expected_text}', "
        f"получили: {response.status_code}, тело: {response.text}"
    )


def assert_response_code_or_text_contains(response, expected_code, expected_text, context):
    try:
        data = response.json()
        code = data.get("responseCode")
    except ValueError:
        code = None

    assert str(code) == str(expected_code) or expected_text.lower() in response.text.lower(), (
        f"{context}: ожидали responseCode {expected_code} или текст '{expected_text}', "
        f"получили тело: {response.text}"
    )
