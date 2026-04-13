import random
import string
from pathlib import Path

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
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
