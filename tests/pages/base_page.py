from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tests.conftest import DEFAULT_WAIT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_WAIT)

    def wait_for_preloader(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.preloader")))

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))