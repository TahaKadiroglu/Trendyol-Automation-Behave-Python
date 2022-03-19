from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser(object):
    driver_path = "C:/Users/Asus/Downloads/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path)
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    driver.maximize_window()

    def close(context):
        context.driver.quit()

