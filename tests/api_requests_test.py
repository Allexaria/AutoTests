import allure
import pytest

from api_requests_framework import ApiClient

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


@pytest.mark.xfail(reason="API возвращает 200 вместо 405 на POST /productsList")
def test_post_product_details():
    client = ApiClient()

    with allure.step("POST-запрос на /productsList"):
        response = client.post_products_list()
        print("Status:", response.status_code)
        print("Response body:", response.text)

    with allure.step("Проверка статус-кода (должен быть 405)"):
        assert response.status_code == 405, f"Ожидали 405, а получили {response.status_code}"

    with allure.step("Проверка сообщения об ошибке"):
        assert "not supported" in response.text.lower(), f"Ожидали сообщение об ошибке, получили: {response.text}"

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

@pytest.mark.xfail(reason="Server returns 200 instead of 405 for PUT /brandsList")
def test_put_to_all_brands_list():
    client = ApiClient()

    with allure.step("PUT request on /brandslist"):
        response = client.put_to_all_brands_list()
        print("Status:", response.status_code)
        print("Response body:", response.text)

    with allure.step("Examination status code is 405(must be 405"):
        assert response.status_code == 405, f"Expect 405, got {response.status_code}"

    with allure.step("JSON response"):
        try:
            data = response.json()
        except ValueError:
            pytest.fail("Response is not JSON")

    with allure.step("Check data structure"):
        assert "brands" in data, "Key 'products' not required"
        assert isinstance(data["brands"], list), "'brands' must be listed"

def test_post_search_product():
    client = ApiClient()

    with allure.step("POST-запрос на /searchProduct с параметром search_product"):
        response = client.post_to_search_product("tshirt")
        print("Status:", response.status_code)
        print("Response body:", response.text)

    with allure.step("Проверка статус-кода (должен быть 200)"):
        assert response.status_code == 200, f"Ожидали 200, а получили {response.status_code}"

    with allure.step("Проверка JSON-ответа"):
        data = response.json()

    with allure.step("Проверка структуры данных"):
        assert "products" in data, "Ключ 'products' отсутствует"
        assert isinstance(data["products"], list), "'products' должен быть списком"

@pytest.mark.xfail(reason = "Server returns 200 instead of 400 for POST /productsList")
def test_post_to_search_products_without_search_product_parameter():
    client = ApiClient()

    with allure.step("POST request on /searchProducts without search_product"):
        response = client.post_without_search(payload={})
        print("Status:", response.status_code)
        print("Response body:", response.text)

    with allure.step("Verify status code is 400(must be 400)"):
        assert response.status_code == 400, f"Expect 400, got {response.status_code}"

    with allure.step("Проверка текста ошибки в ответе"):
        assert "search_product parameter is missing" in response.text.lower(), \
            f"Ожидали сообщение об отсутствии параметра, получили: {response.text}"
