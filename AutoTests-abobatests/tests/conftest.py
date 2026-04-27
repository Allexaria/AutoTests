import os
import random
import string
from pathlib import Path

import pytest
from selenium import webdriver


def _is_truthy(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    chrome_bin = os.environ.get("CHROME_BIN", "").strip()
    if chrome_bin:
        options.binary_location = chrome_bin
    if _is_truthy("SELENIUM_HEADLESS"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    if not _is_truthy("SELENIUM_HEADLESS"):
        window_x = int(os.getenv("AE_WINDOW_X", "1920"))
        window_y = int(os.getenv("AE_WINDOW_Y", "0"))
        window_width = int(os.getenv("AE_WINDOW_WIDTH", "1440"))
        window_height = int(os.getenv("AE_WINDOW_HEIGHT", "920"))
        driver.set_window_rect(
            x=window_x, y=window_y, width=window_width, height=window_height
        )
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd(
        "Network.setBlockedURLs",
        {
            "urls": [
                "*doubleclick.net/*",
                "*googlesyndication.com/*",
                "*googleadservices.com/*",
                "*adservice.google.com/*",
                "*adnxs.com/*",
            ]
        },
    )
    yield driver
    driver.quit()


@pytest.fixture
def random_email():
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(["example.com", "testmail.com", "mail.ru", "gmail.com", "aboba.com"])
    return f"{username}@{domain}"


@pytest.fixture
def random_username():
    first_names = [
        "John",
        "Mira",
        "Anton",
        "Luna",
        "Markus",
        "Elena",
        "David",
        "Sasha",
        "Olga",
        "Leo",
    ]
    last_names = [
        "Steel",
        "Donnelly",
        "Cabaleron",
        "Foster",
        "Ivanov",
        "Kuznetsova",
        "Torres",
        "White",
        "Chen",
        "Ford",
    ]
    return f"{random.choice(first_names)} {random.choice(last_names)}"


@pytest.fixture
def test_file():
    return (Path(__file__).parent / "resources" / "test_image.png").resolve()
