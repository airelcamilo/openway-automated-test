from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage
from tests.pages.detail_page import DetailPage

class HomePage(BasePage):
    PRODUCT_IMAGE_SELECTOR = (By.CSS_SELECTOR, "div.product-img > a")

    def open_page(self):
        self.driver.get("https://www.periplus.com/")

    def open_product_detail_by_index(self, index):
        self.wait_for_preloader()
        self.driver.find_elements(*self.PRODUCT_IMAGE_SELECTOR)[index].click()
        return DetailPage(self.driver)