from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage  

class DetailPage(BasePage):
    CART_BTN_SELECTOR = (By.CSS_SELECTOR, ".btn.btn-add-to-cart")
    MODAL_BTN_SELECTOR = (By.CSS_SELECTOR, ".btn.btn-modal-close.close")

    def click_add_to_cart_button(self):
        self.wait_for_preloader()
        self.driver.find_element(*self.CART_BTN_SELECTOR).click()