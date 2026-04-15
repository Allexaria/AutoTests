import allure
import requests
from api_assertions import (
    assert_has_dict_key,
    assert_has_list_key,
    assert_message_contains,
    assert_response_code,
    assert_response_code_as_str,
    assert_response_code_or_text_contains,
    assert_status_code,
    assert_status_or_text_contains,
    parse_json,
)
from faker import Faker
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class ApiClient:
    BASE_URL = "https://automationexercise.com/api"
    fake = Faker()

    def __init__(self, base_url=None):
        self.base_url = (base_url or self.BASE_URL).rstrip("/")
        self.session = requests.Session()

        retry = Retry(
            total=3,
            backoff_factor=0.3,
            status_forcelist=[500, 502, 503],
            allowed_methods=["GET", "POST", "PUT", "DELETE"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get(self, endpoint, **kwargs):
        return self.session.get(f"{self.base_url}/{endpoint}", **kwargs)

    def post(self, endpoint, **kwargs):
        return self.session.post(f"{self.base_url}/{endpoint}", **kwargs)

    def put(self, endpoint, **kwargs):
        return self.session.put(f"{self.base_url}/{endpoint}", **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(f"{self.base_url}/{endpoint}", **kwargs)

    @allure.step("GET /productsList и проверка ответа")
    def verify_get_products_list(self):
        response = self.get("productsList")
        assert_status_code(response, 200, "GET /productsList")
        data = parse_json(response, "GET /productsList")
        assert_has_list_key(data, "products", "GET /productsList")

    @allure.step("POST /productsList и проверка, что метод не поддерживается")
    def verify_post_products_list_returns_405(self):
        response = self.post("productsList", json={})
        assert_status_or_text_contains(response, 405, "not supported", "POST /productsList")

    @allure.step("GET /brandsList и проверка структуры")
    def verify_get_all_brands_list(self):
        response = self.get("brandsList")
        assert_status_code(response, 200, "GET /brandsList")
        data = parse_json(response, "GET /brandsList")
        assert_has_list_key(data, "brands", "GET /brandsList")

    @allure.step("PUT /brandsList и проверка ошибки в теле ответа (responseCode 405)")
    def verify_put_to_all_brands_list_returns_405(self):
        response = self.put("brandsList")
        data = parse_json(response, "PUT /brandsList")
        assert_response_code_as_str(data, 405, "PUT /brandsList")
        assert_message_contains(data, "not supported", "PUT /brandsList")

    @allure.step("POST /searchProduct с валидным параметром")
    def verify_search_product(self, search_product):
        payload = {"search_product": search_product}
        response = self.post("searchProduct", data=payload)
        assert_status_code(response, 200, "POST /searchProduct")
        data = parse_json(response, "POST /searchProduct")
        assert_has_list_key(data, "products", "POST /searchProduct")

    @allure.step("POST /searchProduct без параметров — проверка ошибки в теле (missing param)")
    def verify_post_without_search_product_param(self):
        response = self.post("searchProduct")
        assert_response_code_or_text_contains(
            response,
            400,
            "search_product parameter is missing",
            "POST /searchProduct without parameter",
        )

    @allure.step("POST /verifyLogin — проверка успешного логина")
    def verify_login_with_valid_details(self, email, password):
        response = self.post("verifyLogin", data={"email": email, "password": password})

        data = parse_json(response, "POST /verifyLogin")
        assert_response_code(data, 200, "POST /verifyLogin")
        assert_message_contains(data, "user exists", "POST /verifyLogin")

    @allure.step("POST /createAccount — создание нового пользователя с фейковыми данными")
    def post_create_account(self):
        name = self.fake.first_name()
        email = self.fake.unique.email()
        password = self.fake.password()
        title = self.fake.random_element(elements=("Mr", "Mrs", "Miss"))
        birth_date = str(self.fake.random_int(min=1, max=28))
        birth_month = self.fake.month_name()
        birth_year = str(self.fake.random_int(min=1950, max=2005))
        firstname = self.fake.first_name()
        lastname = self.fake.last_name()
        company = self.fake.company()
        address1 = self.fake.street_address()
        address2 = self.fake.secondary_address()
        country = self.fake.country()
        zipcode = self.fake.postcode()
        state = self.fake.state()
        city = self.fake.city()
        mobile_number = self.fake.phone_number()

        response = self.post(
            "createAccount",
            data={
                "name": name,
                "email": email,
                "password": password,
                "title": title,
                "birth_date": birth_date,
                "birth_month": birth_month,
                "birth_year": birth_year,
                "firstname": firstname,
                "lastname": lastname,
                "company": company,
                "address1": address1,
                "address2": address2,
                "country": country,
                "zipcode": zipcode,
                "state": state,
                "city": city,
                "mobile_number": mobile_number,
            },
        )

        data = parse_json(response, "POST /createAccount")
        assert_response_code(data, 201, "POST /createAccount")
        assert_message_contains(data, "user created", "POST /createAccount")
        return email, password

    @allure.step("DELETE /deleteAccount — удаление пользователя")
    def delete_account(self, email, password):
        response = self.delete("deleteAccount", data={"email": email, "password": password})
        data = parse_json(response, "DELETE /deleteAccount")
        assert_response_code(data, 200, "DELETE /deleteAccount")
        assert_message_contains(data, "account deleted", "DELETE /deleteAccount")

        return response

    @allure.step("POST /verifyLogin — проверка отсутствия email")
    def verify_login_without_email(self, password):
        response = self.post("verifyLogin", data={"password": password})
        data = parse_json(response, "POST /verifyLogin without email")
        assert_response_code(data, 400, "POST /verifyLogin without email")
        assert_message_contains(data, "parameter is missing", "POST /verifyLogin without email")

    @allure.step("POST /verifyLogin — проверка неверного метода")
    def verify_login_wrong_method(self, email, password):
        response = self.delete("verifyLogin", data={"email": email, "password": password})

        data = parse_json(response, "DELETE /verifyLogin")
        assert_response_code(data, 405, "DELETE /verifyLogin")
        assert_message_contains(data, "this request method is not supported", "DELETE /verifyLogin")

    @allure.step("POST /verifyLogin проверка невалидные данные")
    def verify_login_with_wrong_credentials(self, email, password):
        response = self.post("verifyLogin", data={"email": email, "password": password})
        data = parse_json(response, "POST /verifyLogin wrong credentials")
        assert_response_code(data, 404, "POST /verifyLogin wrong credentials")
        assert_message_contains(data, "user not found", "POST /verifyLogin wrong credentials")

    @allure.step("PUT /updateAccount — обновление данных пользователя")
    def put_update_account(self, **kwargs):
        response = self.put("updateAccount", data=kwargs)
        data = parse_json(response, "PUT /updateAccount")
        assert_response_code(data, 200, "PUT /updateAccount")
        assert_message_contains(data, "user updated", "PUT /updateAccount")

        return response

    @allure.step("GET /getUserDetailByEmail — детали пользователя по email")
    def verify_get_user_detail_by_email(self, email):
        response = self.get("getUserDetailByEmail", params={"email": email})

        assert_status_code(response, 200, "GET /getUserDetailByEmail")
        data = parse_json(response, "GET /getUserDetailByEmail")
        assert_response_code(data, 200, "GET /getUserDetailByEmail")
        assert_has_dict_key(data, "user", "GET /getUserDetailByEmail")

        return data
