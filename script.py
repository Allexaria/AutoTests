import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture
def driver():
    chrome_options = Options()

    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--microphone=allow")
    chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_ya_ru(driver):
    driver.get('https://ya.ru/')
    a = driver.find_element(By.XPATH, '/html/body').text
    name_input = driver.find_element(By.XPATH, '//*[@class="search3__input mini-suggest__input"]')
    assert 'Установить' in a

def test_microphone(driver):
    driver.get('https://ya.ru')

    mic_button = driver.find_element(By.XPATH, '//*[@class="Button VoiceInput search3__voice search3__voice_type_depot VoiceInput_futuris"]')
    mic_button.click()


def test_svg_camera(driver):
    driver.get('https://ya.ru')

    svg_camera = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@class="search3__svg_camera"]')))
    svg_camera.click()

    url_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '(//*[@class="Textinput-Control"])[2]'))
    )
    url_input.send_keys('https://www.ixbt.com/img/n1/news/2024/8/4/RTX5090-HERO-1-1200x624_large.jpg')


    find_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@class="Button Button_view_action Button_width_auto Button_size_m CbirPanelMultimodalUrlForm-Button"]')))
    find_button.click()


    search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="Button Button_view_action Button_width_auto Button_size_m CbirPanelMultimodalQuery-ButtonSearch"]')))
    search_button.click()




