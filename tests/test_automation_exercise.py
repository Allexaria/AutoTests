from pages.HeilHitler.automation_exercise_page import AutoExercise
from pages.HeilHitler.ya_page import YaPage
import allure
import pytest

@allure.title("Test: Register New User And Delete Account")
@allure.description("Opens main page, signs up, verifies account creation, and deletes it")

@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_open_and_verify(driver):
    ae = AutoExercise(driver)

    with allure.step("Opens main page"):
        ae.open_and_verify()

    with allure.step("Login Page Verify"):
        ae.login_page_click_verify()

    with allure.step("Signup New User"):
        ae.signup_new_user()

    with allure.step("Fill User INfo"):
        ae.fill_user_info()

    with allure.step("Account Created"):
        ae.account_created()

    with allure.step("Delete Account"):
        ae.delete_account()

@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_login_with_correct_username(driver):
    ae = AutoExercise(driver)

    with allure.step("Opens main page"):
        ae.open_and_verify()

    with allure.step("Login Page"):
        ae.login_page_click_verify()

    with allure.step("Login"):
        ae.fill_email_and_password()

@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_incorrect_login(driver):
    ae = AutoExercise(driver)

    with allure.step("Login Page Verify"):
        ae.open_and_verify()

    with allure.step("Login Page Verify"):
        ae.login_page_click_verify()

    with allure.step("Login Into Account"):
        ae.login_into_account()

@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_logout_user(driver):
    ae = AutoExercise(driver)

    with allure.step("Open And Verify"):
        ae.open_and_verify()

    with allure.step("Login Page Verify"):
        ae.login_page_click_verify()

    with allure.step("Login Into Account Existing"):
        ae.login_into_account_existing()

    with allure.step("Login Button"):
        ae.login_button()

@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_register_with_existing_email(driver):
    ae = AutoExercise(driver)

    with allure.step("Open And Verify"):
        ae.open_and_verify()

    with allure.step("Login Page Verify"):
        ae.login_page_click_verify()

    with allure.step("Fill Email And Name"):
        ae.fill_email_and_name()

    with allure.step("signup_button"):
        ae.signup_button()

    with allure.step("Error User"):
        ae.error_user()

@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_contact_us(driver):
    ae = AutoExercise(driver)

    with allure.step("Open And Verify"):
        ae.open_and_verify()

    with allure.step("Login Page Verify"):
        ae.login_page_click_verify()

    with allure.step("Contact Us Button"):
        ae.contact_us_button()

    with allure.step("Contact Us Mail Button"):
        ae.contact_us_mail()

@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_cases(driver):
    ae = AutoExercise(driver)

    with allure.step("Open Test Cases"):
        ae.open_and_verify()

    with allure.step("Cases Page Click"):
        ae.cases_test()

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_verify_all_products(driver):
    ae = AutoExercise(driver)

    with allure.step("Open All Products"):
        ae.open_and_verify()

    with allure.step("All Products"):
        ae.products_test()

    with allure.step("All Products Details Verified"):
        ae.details()