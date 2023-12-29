from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = 'username'
        self.password_textbox_id = 'password'
        self.login_button_name = 'login'


    def enter_username(self, username):
        login_window = self.driver.find_element(By.ID, self.username_textbox_id)
        login_window.clear()
        login_window.send_keys(username)

    def enter_password(self, password):
        password_window = self.driver.find_element(By.ID, self.password_textbox_id)
        password_window.clear()
        password_window.send_keys(password)

    def click_login(self):
        reg_button = self.driver.find_element(By.NAME, self.login_button_name)
        reg_button.click()

