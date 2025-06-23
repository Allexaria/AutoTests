from pages.HeilHitler.automation_exercise_page import AutoExercise
from pages.HeilHitler.ya_page import YaPage


def test_open_and_verify(driver):
    ae = AutoExercise(driver)
    ae.open_and_verify()
    ae.login_page_click_verify()
    ae.signup_new_user()
    ae.fill_user_info()
    ae.account_created()
    ae.delete_account()

def test_incorrect_login(driver):
    ae = AutoExercise(driver)
    ae.open_and_verify()
    ae.login_page_click_verify()
    ae.login_into_account()

def test_logout_user(driver):
    ae = AutoExercise(driver)
    ae.open_and_verify()
    ae.login_page_click_verify()
    ae.login_into_account_existing()
    ae.login_button()
    ae.logout()

def test_register_with_existing_email(driver):
    ae = AutoExercise(driver)
    ae.open_and_verify()
    ae.login_page_click_verify()
    ae.fill_email_and_name()
    ae.signup_new_user()

def test_contact_us(driver):
    ae = AutoExercise(driver)
    ae.open_and_verify()
    ae.contact_us_button()
    ae.contact_us_mail()
