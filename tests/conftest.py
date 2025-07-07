import sys
import os
import pytest
import random
import string
from selenium import webdriver
from utils.user_generator import generate_random_user
from sqlalchemy.testing import fixture


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
automation_framework_path = os.path.join(project_root, 'automation_framework')

for p in [project_root, automation_framework_path]:
    if p not in sys.path:
        sys.path.insert(0, p)

print("sys.path:", sys.path)

from api_request.api_requests_framework import ApiClient
from pages.HeilHitler.automation_exercise_page import AutoExercise



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['example.com', 'testmail.com', 'mail.ru', 'gmail.com', 'aboba.com'])
    return f"{username}@{domain}"


@pytest.fixture
def random_username():
    first_names = ['John', 'Mira', 'Anton', 'Luna', 'Markus', 'Elena', 'David', 'Sasha', 'Olga', 'Leo']
    last_names = ['Steel', 'Donnelly', 'Cabaleron', 'Foster', 'Ivanov', 'Kuznetsova', 'Torres', 'White', 'Chen', 'Ford']
    return f"{random.choice(first_names)} {random.choice(last_names)}"
