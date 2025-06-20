import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages.HeilHitler.ya_page import YaPage
import time



def test_ya_ru(driver):
    ya = YaPage(driver)
    ya.open()

def test_microphone(driver):
    ya = YaPage(driver)
    ya.mic()



def test_svg_camera(driver):
    ya = YaPage(driver)
    ya.open()
    ya.svg_camera()

    url = 'https://www.ixbt.com/img/n1/news/2024/8/4/RTX5090-HERO-1-1200x624_large.jpg'
    ya.image_url(url)

    ya.find_button()

    ya.search_button()


def test_empty_search_query(driver):
    ya = YaPage(driver)
    ya.open()
    ya.perform_empty_search()

def test_invalid_image_url_returns_error(driver):
    ya = YaPage(driver)
    ya.open()
    ya.svg_camera()

    invalid_url = "https://www.gutenberg.org/cache/epub/76339/pg76339-images.html"
    ya.image_url(invalid_url)

    ya.find_button()
    ya.error_message()

def test_long_image_url(driver):
    ya = YaPage(driver)
    ya.open()
    ya.svg_camera()
    long_url = 'https://www.ixbt.com/img/n1/news/2024/8/4/RTX5090-HERO-1-1200x624_large.jpg' + "a" * 10000
    ya.image_url(long_url)
    ya.find_button()
    ya.error_message()

def test_search(driver):
    ya = YaPage(driver)
    ya.open()
    ya.input_search("Гитлер моя война")
    ya.press_enter()
    ya.wait_for_search_results()
