import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class AutoExercise:
    def __init__(self, driver):
        self.driver = driver

    def open_and_verify (self):
        self.driver.get('https://automationexercise.com/')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Website for automation practice']"))
        )
        assert self.driver.current_url == 'https://automationexercise.com/'

    def login_page_click_verify(self):
        login_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/login']"))
        )
        login_link.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="signup-form"]'))
        )

    def signup_new_user(self):
        name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-qa='signup-name']"))
        )
        name_field.click()
        name_field.send_keys("Anton Trump Cabaleron")

        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-qa='signup-email']"))
        )
        email_field.click()
        email_field.send_keys("ilikehotgirls@trump.com")

        signup_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-qa='signup-button']"))
        )
        signup_button.click()

        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//h2[@class='title text-center']"))
        )
        text = element.text.strip()
        assert text == "ENTER ACCOUNT INFORMATION", f"Текст заголовка отличается: «{text}»"

    def fill_user_info(self):
        wait = WebDriverWait(self.driver, 10)

        # Title
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='uniform-id_gender1']"))).click()

        # Password
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
        password_field.click()
        password_field.send_keys("12345678Aa")

        # Birthdate: Day, Month, Year
        day_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='days']")))
        day_field.click()
        day_field.send_keys("15", Keys.ENTER)

        month_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='months']")))
        month_field.click()
        month_field.send_keys("Sep", Keys.ENTER)

        year_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='years']")))
        year_field.click()
        year_field.send_keys("1984", Keys.ENTER)

        # Checkboxes
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='newsletter']"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='optin']"))).click()

        # Address fields
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='first_name']"))).send_keys("Anton")
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='last_name']"))).send_keys("Ban")
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='company']"))).send_keys("Dera")
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='address1']"))).send_keys("st. Kyiv, д. 69")
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='address2']"))).send_keys("st. Obolon, д.37")

        # Country dropdown
        country_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='country']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", country_field)
        country_field.click()
        country_field.send_keys("United States", Keys.ENTER)

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='state']"))).send_keys("-")
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='city']"))).send_keys("Sumi")
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='zipcode']"))).send_keys("202017")
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mobile_number']"))).send_keys("+69 88 567 84 93")
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-qa='create-account']"))).click()
        element2 = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='title text-center']"))
        )
        text = element2.text.strip()
        assert text == "ACCOUNT CREATED!", f"Текст заголовка отличается: «{text}»"

    def account_created(self):
        cont = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-qa='continue-button']"))
        )
        cont.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='nav navbar-nav']"))
        )
        text = element.text.strip()
        assert "Anton Ban Dera" in text, f"Ожидали увидеть 'Anton Ban Dera' в тексте, но получили: «{text}»"

    def delete_account(self):
        delete = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/delete_account']"))
        )
        delete.click()
        element = WebDriverWait(self.driver, 10).until(
           EC.presence_of_element_located((By.XPATH, "//*[@class='title text-center']"))
        )
        assert element.text.strip() == "ACCOUNT DELETED!", \
            f"Ожидали текст 'ACCOUNT DELETED!', но получили: «{element.text.strip()}»"

        cont = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-qa='continue-button']"))
        )
        cont.click()

    def login_into_account(self):
        login = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-qa="login-email"]'))
        )
        login.click()
        login.send_keys("notidentifieduser@psina.com")

        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-qa="login-password"]'))
        )
        password.click()
        password.send_keys("unidentifiedpassword000")

        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-qa="login-button"]'))
        )
        login_button.click()

        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[contains(text(),"incorrect")]'))
        )

    def logout(self):
        logout = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/logout']"))
        )
        logout.click()

    def fill_email_and_name(self):
        fill_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-qa="signup-name"]'))
        )
        fill_name.click()
        fill_name.send_keys("Anton Ban Dera")

        fill_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-qa="signup-email"]'))
        )
        fill_email.click()
        fill_email.send_keys("antoniobandera@gmail.com")

    def signup_button(self):
        signup = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-qa="signup-button"]'))
        )
        signup.click()

    def contact_us_button(self):
        contact = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/contact-us']"))
        )
        contact.click()

    def contact_us_mail(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-qa="name"]'))).send_keys("Anton Ban Dera")
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-qa="email"]'))).send_keys(
            "antoniobandera@gmail.com")
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-qa="subject"]'))).send_keys("test if working")
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-qa="message"]'))).send_keys("test if working")

        wait.until(EC.presence_of_element_located((By.NAME, 'upload_file'))).send_keys(
            r"C:\Users\Twelve\Pictures\Screenshots\Снимок экрана (31).png"
        )

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-qa="submit-button"]'))).click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/']"))).click()

    def login_button(self):
        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@data-qa="login-button"]'))
        )
        login.click()

    def login_into_account_existing(self):
            login = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@data-qa="login-email"]'))
            )
            login.click()
            login.send_keys("antoniobandera@gmail.com")

            password = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@data-qa="login-password"]'))
            )
            password.click()
            password.send_keys("12345678Aa")

    def error_user(self):
        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//p[contains(text(), "Email Address already exist")]')
            )
        )

        assert "Email Address already exist" in error.text