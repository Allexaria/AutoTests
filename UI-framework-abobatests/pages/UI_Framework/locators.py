from selenium.webdriver.common.by import By


class AutoExerciseLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    SIGNUP_FORM = (By.CSS_SELECTOR, ".signup-form")

    SIGNUP_NAME = (By.CSS_SELECTOR, "[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "[data-qa='signup-button']")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-qa='continue-button']")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-qa='login-button']")

    CART_BUTTON = (By.CSS_SELECTOR, "a[href='/view_cart']")
    PAY_BUTTON = (By.CSS_SELECTOR, "[data-qa='pay-button']")
    PAYMENT_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success.alert")
