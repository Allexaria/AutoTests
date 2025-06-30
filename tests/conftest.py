import pytest, random, string, sys, os
from selenium import webdriver
from utils.user_generator import generate_random_user
from sqlalchemy.testing import fixture

from pages.HeilHitler.automation_exercise_page import AutoExercise

current_dir = os.path.dirname(os.path.abspath(__file__))
automation_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'automation_framework'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'automation_framework')))



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


