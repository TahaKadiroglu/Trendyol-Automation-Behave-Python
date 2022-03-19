from browser import Browser
from selenium.webdriver.common.by import By
import time


class ProductPageLocator(object):
    RIGHTCLICK = (By.XPATH, "//div[@class='gallery-container']/div/i[1]")
    MORECOMMENTS = (By.XPATH, "//span[contains(text(), 'DAHA FAZLA YORUM GÖSTER')]")
    SEPETEEKLE = (By.XPATH, "//div[@class='add-to-bs-tx']")
    SEPETEGIT = (By.XPATH, "//p[normalize-space()='Sepetim']")


class ProductPage(Browser):
    def changethewindow(self):
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)

    def checkoutthephotos(self):
        self.driver.find_element(*ProductPageLocator.RIGHTCLICK).click()
        self.driver.find_element(*ProductPageLocator.RIGHTCLICK).click()
        self.driver.find_element(*ProductPageLocator.RIGHTCLICK).click()
        self.driver.find_element(*ProductPageLocator.RIGHTCLICK).click()

    def morecomments(self):
         self.driver.find_element(*ProductPageLocator.MORECOMMENTS).click()

    def scrollpage(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def sepeteekle(self):
        self.driver.find_element(*ProductPageLocator.SEPETEEKLE).click()
        time.sleep(3)
        self.driver.find_element(*ProductPageLocator.SEPETEGIT).click()


