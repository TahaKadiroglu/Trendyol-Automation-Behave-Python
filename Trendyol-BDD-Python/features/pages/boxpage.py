from browser import Browser
from selenium.webdriver.common.by import By
import time


class BoxPageLocator(object):
    TRASH = (By.CLASS_NAME, "i-trash")
    DELETEPRODUCT = (By.XPATH, "//button[normalize-space()='Sil']")


class BoxPage(Browser):

    def trash(self):
        self.driver.find_element(*BoxPageLocator.TRASH).click()
        time.sleep(5)
        self.driver.find_element(*BoxPageLocator.DELETEPRODUCT).click()
