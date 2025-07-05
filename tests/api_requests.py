from unittest import expectedFailure
import sys
import os


sys.path.insert(0, r"C:\Users\Twelve\PycharmProjects\api_requests")
import requests
import allure
import pytest
import json

from api_request.api_tests.clients import ApiClient
from faker import Faker

def test_api_product_list():
    client = ApiClient()

    with allure.step("Отправка GET-запроса на /productsList"):
        response = client.get_products_list()

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200, f"Ожидали 200, а получили {response.status_code}"

    with allure.step("Проверка, что ответ — JSON"):
        try:
            data = response.json()
        except ValueError:
            pytest.fail("Ответ не является JSON")

    with allure.step("Проверка структуры данных"):
        assert "products" in data, "Ключ 'products' отсутствует"
        assert isinstance(data["products"], list), "'products' должен быть списком"


def test_post_product_details():
    client = ApiClient()

    with allure.step("POST-запрос на /productsList"):
        response = client.post_products_list()
        print("Status:", response.status_code)
        print("Response body:", response.text)
        response_json = response.json()

    with allure.step("Проверка HTTP статуса (ожидаем 200, так как API так работает)"):
        assert response.status_code == 200, f"Ожидали HTTP 200, получили {response.status_code}"

    with allure.step("Проверка внутреннего кода ошибки (ожидаем 405)"):
        assert response_json.get("responseCode") == 405, \
            f"Ожидали responseCode 405, получили {response_json.get('responseCode')}"

    with allure.step("Проверка сообщения об ошибке"):
        assert "not supported" in response_json.get("message", "").lower(), \
            f"Ожидали сообщение об ошибке 'not supported', получили: {response_json.get('message')}"

def test_get_all_brands_list():
    client = ApiClient()

    with allure.step("GET request on /brandslist"):
        response = client.get_all_brands_list()
        print("Status:", response.status_code)
        print("Response body:", response.text)

    with allure.step("Examination status code is 200(must be 200"):
        assert response.status_code == 200, f"Expect 200, got {response.status_code}"

    with allure.step("JSON response"):
        try:
            data = response.json()
        except ValueError:
            pytest.fail("Response is not JSON")

    with allure.step("Check data structure"):
        assert "brands" in data, "Key 'products' not required"
        assert isinstance(data["brands"], list), "'brands' must be listed"

def test_put_to_all_brands_list():
    client = ApiClient()

    with allure.step("PUT request on /brandslist"):
        response = client.put_to_all_brands_list()
        print("Status:", response.status_code)
        print("Response body:", response.text)

    with allure.step("Verify HTTP status is 200 (API returns 200 even for errors)"):
        assert response.status_code == 200, f"Expect HTTP 200, got {response.status_code}"

    with allure.step("Parse JSON response"):
        try:
            data = response.json()
        except ValueError:
            pytest.fail("Response is not JSON")

    with allure.step("Verify internal responseCode is 405 (method not allowed)"):
        assert data.get("responseCode") == 405, f"Expect responseCode 405, got {data.get('responseCode')}"

    with allure.step("Check data structure for 'brands' key"):
        assert "brands" in data, "Key 'brands' not found in response"
        assert isinstance(data["brands"], list), "'brands' must be a list"

def test_put_to_all_brands_list():
    client = ApiClient()

    with allure.step("PUT request on /brandslist"):
        response = client.put_to_all_brands_list()
        print("Status:", response.status_code)
        print("Response body:", response.text)

    with allure.step("Verify HTTP status is 200 (API returns 200 even for errors)"):
        assert response.status_code == 200, f"Expect HTTP 200, got {response.status_code}"

    with allure.step("Parse JSON response"):
        try:
            data = response.json()
        except ValueError:
            pytest.fail("Response is not JSON")

    with allure.step("Verify internal responseCode"):
        assert data.get("responseCode") == 405, f"Expect responseCode 405, got {data.get('responseCode')}"

    with allure.step("If no error, check data structure for 'brands' key"):
        if data.get("responseCode") == 200:
            assert "brands" in data, "Key 'brands' not found in response"
            assert isinstance(data["brands"], list), "'brands' must be a list"
        else:
            assert "not supported" in data.get("message", "").lower(), \
                f"Expected 'not supported' message, got: {data.get('message')}"

def test_post_to_search_products_without_search_product_parameter():
    client = ApiClient()

    with allure.step("POST request on /searchProducts without search_product"):
        response = client.post_without_search(payload={})
        print("Status:", response.status_code)
        print("Response body:", response.text)
        response_json = response.json()

    with allure.step("Verify HTTP status is 200 (API always returns 200)"):
        assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"

    with allure.step("Verify internal responseCode is 400"):
        assert response_json["responseCode"] == 400, \
            f"Expected responseCode 400, got {response_json.get('responseCode')}"

    with allure.step("Проверка текста ошибки в ответе"):
        assert "search_product" in response_json["message"].lower(), \
            f"Ожидали сообщение об отсутствии параметра, получили: {response_json.get('message')}"
def test_successful_login_after_signup():
    client = ApiClient()

    email = "antoniobandera@gmail.com"
    password = "12345678Aa"

    with allure.step("Login with newly registered user"):
        login_response = client.post_verif_login(email=email, password=password)
        print("Login Status:", login_response.status_code)
        print("Login Body:", login_response.text)
        login_json = login_response.json()

    with allure.step("Verify login is successful"):
        assert login_response.status_code == 200
        assert login_json["responseCode"] == 200
        assert login_json["message"] == "User exists!"

def test_verify_login_without_email_parameter():
    client = ApiClient()

    with allure.step("Login without email"):
        login_response = client.post_verif_login(email=None, password=None)
        print("Login Status:", login_response.status_code)
        print("Login Body:", login_response.text)
        login_json = login_response.json()

    with allure.step("Verify HTTP status is 200 (always 200 from this API)"):
        assert login_response.status_code == 200, \
            f"Expected HTTP 200, got {login_response.status_code}"

    with allure.step("Verify internal responseCode is 400 and error message is correct"):
        assert login_json["responseCode"] == 400, \
            f"Expected responseCode 400, got {login_json['responseCode']}"
        assert "missing" in login_json["message"].lower(), \
            f"Expected missing email/password message, got: {login_json['message']}"
def test_delete_verify_login():
    client = ApiClient()

    with allure.step("DELETE to /api/verifyLogin"):
        login_response = client.delete_login(email=None, password=None)
        print("Login Status:", login_response.status_code)
        print("Login Body:", login_response.text)
        login_json = login_response.json()

    with allure.step("Verify HTTP status is 200 (API always returns 200)"):
        assert login_response.status_code == 200, f"Expected HTTP 200, got {login_response.status_code}"
        f"Expected http 200, got {login_response.text}"

    with allure.step("Verify internal responseCode is 405 and error message is correct"):
        assert login_json["responseCode"] == 405, \
        f"Expected responseCode 405, got {login_json['responseCode']}"
        assert "This request method is not supported" in login_json["message"], f"Expected 'not supported' message, got: {login_json['message']}"

def test_post_to_verify_with_invalid_details():
    client = ApiClient()

    with allure.step("POST to /api/verifyLogin with invalid credentials"):
        login_response = client.post_verif_login(email="nonexistent@example.com", password="wrongpassword")
        print("Login Status:", login_response.status_code)
        print("Login Body:", login_response.text)
        login_json = login_response.json()

    with allure.step("Verify HTTP status is 200 (API always returns 200)"):
        assert login_response.status_code == 200, f"Expected HTTP 200, got {login_response.status_code}"

    with allure.step("Verify internal responseCode is 404 and error message is correct"):
        assert login_json["responseCode"] == 404, f"Expected responseCode 404, got {login_json['responseCode']}"
        assert "User not found" in login_json["message"], f"Expected 'User not found' message, got {login_json['message']}"

def test_create_account_with_generated_data():
    client = ApiClient()
    fake = Faker()

    with allure.step("Generate user data"):
        payload = {
            "name": fake.first_name(),
            "email": fake.unique.email(),
            "password": fake.password(length=10),
            "title": fake.random_element(elements=["Mr", "Mrs", "Miss"]),
            "birth_date": str(fake.random_int(min=1, max=28)),
            "birth_month": str(fake.random_int(min=1, max=12)),
            "birth_year": str(fake.random_int(min=1970, max=2005)),
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "company": fake.company(),
            "address1": fake.street_address(),
            "address2": fake.secondary_address(),
            "country": "Canada",
            "zipcode": fake.postcode(),
            "state": fake.state(),
            "city": fake.city(),
            "mobile_number": fake.phone_number()
        }

        print("Payload:", payload)

    with allure.step("Send POST request to /api/createAccount"):
        response = client.post_create_account(**payload)
        print("HTTP Status:", response.status_code)
        print("Response body:", response.text)

    with allure.step("Verify HTTP status is 200 (API always returns 200)"):
        assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"

    with allure.step("Parse JSON response and validate internal responseCode"):
        try:
            data = response.json()
        except ValueError:
            pytest.fail("Response is not valid JSON")

        assert data.get("responseCode") == 201, f"Expected responseCode 201, got {data.get('responseCode')}"
        assert "User created" in data.get("message", ""), f"Expected 'User created' message, got: {data.get('message')}"

def test_create_and_delete_user_account():
    client = ApiClient()
    fake = Faker()

    user_data = {
        "name": fake.first_name(),
        "email": fake.unique.email(),
        "password": fake.password(length=10),
        "title": fake.random_element(elements=["Mr", "Mrs", "Miss"]),
        "birth_date": str(fake.random_int(min=1, max=28)),
        "birth_month": str(fake.random_int(min=1, max=12)),
        "birth_year": str(fake.random_int(min=1970, max=2005)),
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "Canada",
        "zipcode": fake.postcode(),
        "state": fake.state(),
        "city": fake.city(),
        "mobile_number": fake.phone_number()
    }

    email = user_data["email"]
    password = user_data["password"]

    with allure.step("Create account with random data"):
        create_response = client.post_create_account(**user_data)
        print("Create status:", create_response.status_code)
        print("Create body:", create_response.text)

        assert create_response.status_code == 200, f"Expected HTTP 200, got {create_response.status_code}"

        try:
            create_json = create_response.json()
        except ValueError:
            pytest.fail("Create response is not JSON")

        assert create_json.get("responseCode") == 201, f"Expected responseCode 201, got {create_json.get('responseCode')}"
        assert "User created" in create_json.get("message", ""), f"Expected success message, got {create_json.get('message')}"

    with allure.step("Delete the created account"):
        delete_response = client.delete_to_delete_account(email=email, password=password)
        print("Delete status:", delete_response.status_code)
        print("Delete body:", delete_response.text)

        assert delete_response.status_code == 200, f"Expected HTTP 200, got {delete_response.status_code}"

        try:
            delete_json = delete_response.json()
        except ValueError:
            pytest.fail("Delete response is not JSON")

        assert delete_json.get("responseCode") == 200, f"Expected responseCode 200, got {delete_json.get('responseCode')}"
        assert "Account deleted!" in delete_json.get("message", ""), f"Expected deletion message, got {delete_json.get('message')}"

def test_put_to_update_user_account():
    client = ApiClient()
    fake = Faker()

    user_data = {
        "name": fake.first_name(),
        "email": fake.unique.email(),
        "password": fake.password(length=10),
        "title": fake.random_element(elements=["Mr", "Mrs", "Miss"]),
        "birth_date": str(fake.random_int(min=1, max=28)),
        "birth_month": str(fake.random_int(min=1, max=12)),
        "birth_year": str(fake.random_int(min=1970, max=2005)),
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "Canada",
        "zipcode": fake.postcode(),
        "state": fake.state(),
        "city": fake.city(),
        "mobile_number": fake.phone_number()
    }

    email = user_data["email"]
    password = user_data["password"]

    with allure.step("Create account with random data"):
        create_response = client.post_create_account(**user_data)
        print("Create status:", create_response.status_code)
        print("Create body:", create_response.text)

        assert create_response.status_code == 200, f"Expected HTTP 200, got {create_response.status_code}"

        try:
            create_json = create_response.json()
        except ValueError:
            pytest.fail("Create response is not JSON")

        assert create_json.get(
            "responseCode") == 201, f"Expected responseCode 201, got {create_json.get('responseCode')}"
        assert "User created" in create_json.get("message",
                                                 ""), f"Expected success message, got {create_json.get('message')}"

    with allure.step("PUT to update account with random data"):
        response = client.put_to_update_user_account(**user_data)
        print("HTTP Status:", response.status_code)
        print("Response body:", response.text)
        assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
        assert "User updated!" in response.text, f"Expected success message, got {response.text}"

def test_get_user_details_by_email():
    client = ApiClient()
    fake = Faker()

    user_data = {
        "name": fake.first_name(),
        "email": fake.unique.email(),
        "password": fake.password(length=10),
        "title": fake.random_element(elements=["Mr", "Mrs", "Miss"]),
        "birth_date": str(fake.random_int(min=1, max=28)),
        "birth_month": str(fake.random_int(min=1, max=12)),
        "birth_year": str(fake.random_int(min=1970, max=2005)),
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "Canada",
        "zipcode": fake.postcode(),
        "state": fake.state(),
        "city": fake.city(),
        "mobile_number": fake.phone_number()
    }

    email = user_data["email"]
    password = user_data["password"]

    with allure.step("Create account with random data"):
        create_response = client.post_create_account(**user_data)
        print("Create status:", create_response.status_code)
        print("Create body:", create_response.text)

        assert create_response.status_code == 200, f"Expected HTTP 200, got {create_response.status_code}"

        try:
            create_json = create_response.json()
        except ValueError:
            pytest.fail("Create response is not JSON")

        assert create_json.get(
            "responseCode") == 201, f"Expected responseCode 201, got {create_json.get('responseCode')}"
        assert "User created" in create_json.get("message",
                                                 ""), f"Expected success message, got {create_json.get('message')}"

    with allure.step("GET user detail by email"):
        response = client.get_to_user_account_detail(email)
        print("HTTP Status:", response.status_code)
        print("Response body:", response.text)

        assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"

        try:
            response_json = response.json()
        except ValueError:
            pytest.fail("GET response is not JSON")

        assert response_json.get(
            "responseCode") == 200, f"Expected responseCode 200, got {response_json.get('responseCode')}"
        assert response_json.get("user", {}).get(
            "email") == email, f"Expected email {email}, got {response_json.get('user', {}).get('email')}"
