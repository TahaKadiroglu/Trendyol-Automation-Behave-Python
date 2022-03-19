from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.customlogger import LogGen
mylog = LogGen.customloggerrr()


class HomePageLocator(object):
    POP_UP = (By.XPATH, "//div[@title='Kapat']")
    GIRIS_YAP = (By.XPATH, "//p[contains(text(),'Giriş Yap')]")
    SEARCHBOX = (By.CLASS_NAME, 'search-box')
    OVERLAY = (By.XPATH, "//div[@class='overlay']")
    FILTRE1 = (By.XPATH, "//div[contains(text(), 'Akıllı Cep Telefonu')]")
    FILTRE2 = (By.XPATH, "//a[@title='Beyaz']")
    FILTRE3 = (By.XPATH, "//div[@data-title='Fiyat']")
    FILTRE4 = (By.XPATH, "//div[@data-title='Fiyat']//a[2]")
    FILTRE5 = (By.XPATH, "//div[@class='prdct-cntnr-wrppr']//div[1]//div[1]//a[1]")


class HomePage(Browser):

    def navigate(self, address):
        self.driver.get(address)

    def search(self):
        self.driver.find_element(*HomePageLocator.POP_UP).click()
        self.driver.find_element(*HomePageLocator.GIRIS_YAP).click()
        mylog.info("Giris Sayfasina Yonlendiriliyorsunuz.")

    def searchforproduct(self):
        self.driver.find_element(*HomePageLocator.SEARCHBOX).send_keys("Iphone 13")
        self.driver.find_element(*HomePageLocator.SEARCHBOX).send_keys(Keys.RETURN)
        mylog.info("Iphone 13 icin arama yapiliyor.")
    def filterproducts(self):
        self.driver.find_element(*HomePageLocator.OVERLAY).click()
        self.driver.find_element(*HomePageLocator.FILTRE1).click()
        self.driver.find_element(*HomePageLocator.FILTRE2).click()
        self.driver.find_element(*HomePageLocator.FILTRE3).click()
        self.driver.find_element(*HomePageLocator.FILTRE4).click()
        self.driver.find_element(*HomePageLocator.FILTRE5).click()





