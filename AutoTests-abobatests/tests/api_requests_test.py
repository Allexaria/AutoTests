import pytest

from qa_project.framework.api import APIClient, CatalogService, UserService
from qa_project.framework.core.data_factory import create_user

pytestmark = [pytest.mark.api]

client = APIClient()
catalog_service = CatalogService(client)
user_service = UserService(client)


@pytest.mark.smoke
def test_api_product_list():
    response, data = catalog_service.get_products_list_validated()
    assert response.status_code == 200
    assert isinstance(data.products, list)


@pytest.mark.smoke
def test_post_product_details():
    response = catalog_service.post_products_list()
    assert response.status_code == 405 or "not supported" in response.text.lower()


@pytest.mark.smoke
def test_get_all_brands_list():
    response = catalog_service.get_brands_list()
    assert response.status_code == 200
    assert isinstance(response.json().get("brands"), list)


@pytest.mark.smoke
def test_put_to_all_brands_list():
    response = catalog_service.put_brands_list()
    assert str(response.json().get("responseCode")) == "405"


@pytest.mark.smoke
def test_post_search_product():
    response = catalog_service.search_product("tshirt")
    assert response.status_code == 200
    assert isinstance(response.json().get("products"), list)


@pytest.mark.smoke
def test_post_to_search_products_without_search_product_parameter():
    response = catalog_service.search_product_without_param()
    data = (
        response.json()
        if response.headers.get("Content-Type", "").startswith("application/json")
        else {}
    )
    assert (
        str(data.get("responseCode")) == "400"
        or "search_product parameter is missing" in response.text.lower()
    )


@pytest.mark.regression
def test_create_and_verify_login_delete():
    user_data = create_user()
    create_response, create_data = user_service.create_account_validated(user_data)
    assert create_data.responseCode == 201

    login_response, login_data = user_service.login_validated(
        email=user_data["email"], password=user_data["password"]
    )
    assert login_data.responseCode == 200

    delete_response, delete_data = user_service.delete_account_validated(
        email=user_data["email"], password=user_data["password"]
    )
    assert delete_data.responseCode == 200


@pytest.mark.smoke
def test_login_without_email():
    response = user_service.login_without_email(password="somepassword123")
    assert response.json().get("responseCode") == 400


@pytest.mark.smoke
def test_verify_login_wrong_method():
    response = user_service.login_wrong_method(email="gagaga", password="123123")
    assert response.json().get("responseCode") == 405


@pytest.mark.smoke
def test_verify_login_with_wrong_credentials():
    response, data = user_service.login_validated(email="gagaga", password="123123")
    assert data.responseCode == 404


@pytest.mark.regression
def test_create_update_delete_user_account():
    user_data = create_user()
    create_response = user_service.create_account(user_data)
    assert create_response.json().get("responseCode") == 201

    email = user_data["email"]
    password = user_data["password"]
    updated_data = {
        "name": user_data["name"],
        "email": email,
        "password": password,
        "title": user_data["title"],
        "birth_date": user_data["birth_date"],
        "birth_month": user_data["birth_month"],
        "birth_year": user_data["birth_year"],
        "firstname": user_data["firstname"],
        "lastname": user_data["lastname"],
        "company": user_data["company"],
        "address1": user_data["address1"],
        "address2": user_data["address2"],
        "country": user_data["country"],
        "zipcode": user_data["zipcode"],
        "state": user_data["state"],
        "city": user_data["city"],
        "mobile_number": user_data["mobile_number"],
    }
    update_response = user_service.update_account(updated_data)
    assert update_response.json().get("responseCode") == 200
    user_service.delete_account(email=email, password=password)


@pytest.mark.regression
def test_get_user_detail_by_email():
    user_data = create_user()
    create_response = user_service.create_account(user_data)
    assert create_response.json().get("responseCode") == 201
    data = user_service.get_user_detail_by_email(email=user_data["email"]).json()

    assert data["user"]["email"] == user_data["email"]

    user_service.delete_account(email=user_data["email"], password=user_data["password"])
