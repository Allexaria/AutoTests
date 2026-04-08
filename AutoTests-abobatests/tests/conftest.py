import os
import random
import string
import sys

import pytest
from selenium import webdriver

# Normalize import paths for sibling framework folders.
current_dir = os.path.dirname(__file__)
workspace_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
project_paths = [
    os.path.join(workspace_root, "AutoTests-abobatests"),
    os.path.join(workspace_root, "UI-framework-abobatests"),
    os.path.join(workspace_root, "API-framework-develope"),
]

for p in project_paths:
    if p not in sys.path:
        sys.path.insert(0, p)


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
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
