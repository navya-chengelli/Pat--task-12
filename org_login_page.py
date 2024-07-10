
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        driver.implicit_wait=50
        self.username_input = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        self.password_input = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        self.login_button = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')


    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class LoginPage:
#     def _init_(self, driver):
#         self.driver = driver
#         self.username_input = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
#         self.password_input = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
#         self.login_button = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
#
#     def set_username(self, username):
#         WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.username_input)).send_keys(username)
#
#     def set_password(self, password):
#         WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.password_input)).send_keys(password)
#
#     def click_login(self):
#         WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.login_button)).click()
