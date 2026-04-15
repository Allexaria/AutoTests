from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Waits:
    @staticmethod
    def present(driver, locator, timeout=10):
        return WebDriverWait(
            driver, timeout, ignored_exceptions=(StaleElementReferenceException,)
        ).until(EC.presence_of_element_located(locator))

    @staticmethod
    def visible(driver, locator, timeout=10):
        return WebDriverWait(
            driver, timeout, ignored_exceptions=(StaleElementReferenceException,)
        ).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def clickable(driver, locator, timeout=10):
        return WebDriverWait(
            driver, timeout, ignored_exceptions=(StaleElementReferenceException,)
        ).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def url_contains(driver, text, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.url_contains(text))

    @staticmethod
    def page_ready(driver, timeout=10):
        return WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
