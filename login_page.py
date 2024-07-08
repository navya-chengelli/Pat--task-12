from selenium.webdriver.common.by import By

class OrangeLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        self.username_input = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')

        self.password_input = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        self.log_in_submit = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')



    def navigate_to_login_page(self):
        self.driver.get(self.url)


    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)


    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.log_in_submit).click()