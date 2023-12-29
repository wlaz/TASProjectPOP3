from selenium import webdriver
from time import sleep
import unittest
from TASProjectPOP3.Tests.login_credentials import LoginCred
from TASProjectPOP3.Tests.login_credentials import PurchaseCred
from TASProjectPOP3.Pages.loginPage import LoginPage
from TASProjectPOP3.Pages.homePage import HomePage
from TASProjectPOP3.Pages.purchasePage import PurchasePage


class TC1(unittest.TestCase):
#logowanie zarejestrowanego użytkownika

    @classmethod
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()


    def test1(self):
        driver=self.driver
        driver.get('https://skleptest.pl//')

        sleep(0)
        homepage = HomePage(driver)
        homepage.click_welcome()

        login = LoginPage(driver)
        login.enter_username(LoginCred.email1)
        login.enter_password(LoginCred.passw1)
        login.click_login()

        homepage.get_loging_confirmation()

        homepage.click_logout()

        sleep(0)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('pass')
    pass

class TC2(unittest.TestCase):
# logowanie niezarejestrowanego użytkownika
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        # logowanie
        driver.get('https://skleptest.pl//')
        sleep(0)
        homepage = HomePage(driver)
        homepage.click_welcome()

        login = LoginPage(driver)
        login.enter_username(LoginCred.email2)
        login.enter_password(LoginCred.passw2)
        login.click_login()

        homepage.get_lackOfRegister_confirmation()

        sleep(0)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('pass')
    pass

class TC3(unittest.TestCase):
#logowanie zarejestrowanego użytkownika z błędnym hasłem
    @classmethod
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver

        driver.get('https://skleptest.pl//')
        sleep(0)
        homepage = HomePage(driver)
        homepage.click_welcome()

        login=LoginPage(driver)
        login.enter_username(LoginCred.email2)
        login.enter_password(LoginCred.passw2)
        login.click_login()

        homepage.get_lackOfRegister_confirmation()

        sleep(0)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('pass')
    pass

class TC4(unittest.TestCase):
# wyszukiwanie produktu po nazwie
    @classmethod
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get('https://skleptest.pl//')
        sleep(0)

        search_product = PurchasePage(driver)
        search_product.search_link(PurchaseCred.search_field)
        search_product.click_search()

        sleep(0)

        search_product.search_check()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('pass')
    pass

class TC5(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        # logowanie
        driver.get('https://skleptest.pl//')
        sleep(0)
        homepage = HomePage(driver)
        homepage.click_welcome()

        login = LoginPage(driver)
        login.enter_username(LoginCred.email1)
        login.enter_password(LoginCred.passw1)
        login.click_login()
        sleep(0)
        search_product = PurchasePage(driver)
        search_product.search_link(PurchaseCred.search_field)
        search_product.click_search()
        search_product.blue_shoes()
        search_product.quantity_shoes()
        search_product.toThe_card()

        purchase = PurchasePage(driver)
        purchase.purchase_check()

        sleep(0)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('pass')
    pass
