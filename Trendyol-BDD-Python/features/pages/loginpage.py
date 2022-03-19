from browser import Browser
from selenium.webdriver.common.by import By


class LoginPageLocator(object):
    E_MAIL = (By.ID, 'login-email')
    PASSWORD = (By.ID, 'login-password-input')
    LOGIN = (By.XPATH, "//button[@type='submit']//span[contains(text(),'Giriş Yap')]")


class LoginPage(Browser):
    def email(self, username):
        self.driver.find_element(*LoginPageLocator.E_MAIL).send_keys(username)

    def password(self, password):
        self.driver.find_element(*LoginPageLocator.PASSWORD).send_keys(password)

    def search(self):
        self.driver.find_element(*LoginPageLocator.LOGIN).click()

