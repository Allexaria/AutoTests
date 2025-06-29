import pytest
import sys
import os
from selenium import webdriver
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



@fixture
def random_email():
    return AutoExercise.generate_random_email()