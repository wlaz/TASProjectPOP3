from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.account_link_linkText = 'Account'
        self.logout_link_XPath = "//a[contains(text(),'Log out')]"
        self.search_link_ID = 'search-top-bar-submit'

    def click_welcome(self):
        search_account_button = self.driver.find_element(By.LINK_TEXT, self.account_link_linkText)
        search_account_button.click()

    def click_logout(self):
        logout = self.driver.find_element(By.XPATH, self.logout_link_XPath)
        logout.click()

    def get_loging_confirmation(self):
        login_confirmation = self.driver.find_element(By.XPATH, self.logout_link_XPath)
        login_content = login_confirmation.text
        if len(login_content) == 0:
            return print('Użytkownik niezalogowany')
        else:
            return print('Użytkownik został zalogowany')

    def get_lackOfRegister_confirmation(self):
        lackOfRegister = self.driver.find_element(By.XPATH, "//strong[contains(text(),'Error:')]")
        lackOfRegister_content = lackOfRegister.text
        if len(lackOfRegister_content) ==0:
            return print('Uzytkownik zalogowany')
        else:
            return print("Użytkownik niezalogowane")