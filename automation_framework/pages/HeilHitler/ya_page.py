from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time

class YaPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://ya.ru')

    def get_body_text(self):
        return self.driver.find_element(By.XPATH, '/html/body').text

    def input_search(self, text):
        search_input = self.driver.find_element(By.XPATH, '//*[@class="search3__input mini-suggest__input"]')
        search_input.clear()
        search_input.send_keys(text)

    def mic(self):
        self.driver.get('https://ya.ru')

        mic_button = self.driver.find_element(By.XPATH,
                                         '//*[@class="Button VoiceInput search3__voice search3__voice_type_depot VoiceInput_futuris"]')
        mic_button.click()

    def svg_camera(self):
        svg_camera = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="search3__svg_camera"]'))
        )
        svg_camera.click()

    def image_url(self, url):
        url_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//*[@class="Textinput-Control"])[2]'))
        )
        url_input.clear()
        url_input.send_keys(url)

    def find_button(self):
        find_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="Button Button_view_action Button_width_auto Button_size_m CbirPanelMultimodalUrlForm-Button"]'))
        )
        find_button.click()

    def search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="Button Button_view_action Button_width_auto Button_size_m CbirPanelMultimodalQuery-ButtonSearch"]'))
        )
        search_button.click()


    def perform_empty_search(self):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search3__input"))
        )
        search_input.clear()
        search_input.send_keys("\n")
        return search_input

    def error_message(self):
        txt_error = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="SnackbarTransitioned-Content"]'))
        )
        return txt_error.text

    def press_enter(self):
        search_input = self.driver.find_element(By.XPATH, '//*[@class="search3__input mini-suggest__input"]')
        search_input.send_keys(Keys.ENTER)

    def wait_for_search_results(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.serp-list'))
        )
