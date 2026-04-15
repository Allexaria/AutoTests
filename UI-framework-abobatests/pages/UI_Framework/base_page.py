from selenium.common.exceptions import StaleElementReferenceException

from pages.UI_Framework.waits import Waits


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def _normalize_locator(*locator):
        # Support both styles: (By.ID, "x") and ((By.ID, "x"),)
        if len(locator) == 1 and isinstance(locator[0], tuple):
            return locator[0]
        if len(locator) == 2:
            return locator
        raise ValueError("Locator must be a tuple (by, value) or two arguments: by, value")

    def wait_visible(self, locator, timeout=10):
        locator = self._normalize_locator(locator)
        return Waits.visible(self.driver, locator, timeout)

    def wait_present(self, locator, timeout=10):
        locator = self._normalize_locator(locator)
        return Waits.present(self.driver, locator, timeout)

    def wait_clickable(self, locator, timeout=10):
        locator = self._normalize_locator(locator)
        return Waits.clickable(self.driver, locator, timeout)

    def click(self, locator, timeout=10):
        locator = self._normalize_locator(locator)
        for attempt in range(2):
            try:
                self.wait_clickable(locator, timeout).click()
                return
            except StaleElementReferenceException:
                if attempt == 1:
                    raise

    def safe_click(self, *locator, timeout=10):
        hide_ads = getattr(self, "hide_ads", None)
        if callable(hide_ads):
            hide_ads()
        normalized_locator = self._normalize_locator(*locator)
        for attempt in range(2):
            try:
                element = self.wait_clickable(normalized_locator, timeout)
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", element
                )
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == 1:
                    raise

    def wait_url_contains(self, text, timeout=10):
        return Waits.url_contains(self.driver, text, timeout)

    def wait_page_ready(self, timeout=10):
        return Waits.page_ready(self.driver, timeout)

    def type(self, locator, value, timeout=10, clear_first=False):
        element = self.wait_visible(locator, timeout)
        if clear_first:
            element.clear()
        element.send_keys(value)
        return element
