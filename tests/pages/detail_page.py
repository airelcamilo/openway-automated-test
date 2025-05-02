from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.base_page import BasePage  

class DetailPage(BasePage):
    CART_BTN_SELECTOR = (By.CSS_SELECTOR, ".btn.btn-add-to-cart")
    MODAL_SELECTOR = (By.ID, "Notification-Modal")
    PRODUCT_NAME_SELECTOR = (By.CSS_SELECTOR, "div.col-lg-5.col-md-5.col-12.quickview-content > h2")
    PRODUCT_ISBN_XPATH = (By.XPATH, "//p[text()='ISBN-13']/following-sibling::p")

    def click_add_to_cart_button(self):
        self.wait_for_preloader()
        self.driver.find_element(*self.CART_BTN_SELECTOR).click()
        self.wait.until(EC.visibility_of_element_located(self.MODAL_SELECTOR))
        self.wait.until(EC.invisibility_of_element_located(self.MODAL_SELECTOR))

    def get_product_name(self):
        self.wait_for_preloader()
        return self.driver.find_element(*self.PRODUCT_NAME_SELECTOR).text.strip()
        
    def get_product_isbn(self):
        self.wait_for_preloader()
        return self.driver.find_element(*self.PRODUCT_ISBN_XPATH).text.strip()