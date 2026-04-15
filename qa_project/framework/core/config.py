import os


class Config:
    API_BASE_URL = os.getenv("API_BASE_URL", "https://automationexercise.com/api")
    UI_BASE_URL = os.getenv("UI_BASE_URL", "https://automationexercise.com/")
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
