from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FacebookLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, 'email')
        self.password_input = (By.ID, 'pass')
        self.login_button = (By.ID, 'loginbutton')

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

class FacebookHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.user_menu = (By.ID, 'userNavigationLabel')

    def is_user_menu_visible(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.user_menu))

def test_successful_login():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path='C:/Users/Roman/Desktop/folder/chromedriver.exe', options=options)
    driver.get('https://www.facebook.com/')

    login_page = FacebookLoginPage(driver)
    login_page.enter_email('your_valid_email')
    login_page.enter_password('your_valid_password')
    login_page.click_login_button()

    home_page = FacebookHomePage(driver)
    assert home_page.is_user_menu_visible()

    driver.quit()

def test_invalid_credentials():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path='C:/Users/Roman/Desktop/folder/chromedriver.exe', options=options)
    driver.get('https://www.facebook.com/')

    login_page = FacebookLoginPage(driver)
    login_page.enter_email('your_invalid_email')
    login_page.enter_password('your_invalid_password')
    login_page.click_login_button()

    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))
    assert error_message.text == 'Adresa de e-mail sau numărul de telefon pe care le-ai introdus nu corespund niciunui cont. Înregistrează-te pentru un cont.'

    driver.quit()

# Run both tests
test_successful_login()
test_invalid_credentials()
