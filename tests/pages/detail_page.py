from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.base_page import BasePage  

class DetailPage(BasePage):
    CART_BTN_SELECTOR = (By.CSS_SELECTOR, ".btn.btn-add-to-cart")
    MODAL_SELECTOR = (By.ID, "Notification-Modal")

    def click_add_to_cart_button(self):
        self.wait_for_preloader()
        self.driver.find_element(*self.CART_BTN_SELECTOR).click()
        self.wait.until(EC.visibility_of_element_located(self.MODAL_SELECTOR))
        self.wait.until(EC.invisibility_of_element_located(self.MODAL_SELECTOR))