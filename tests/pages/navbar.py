from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys

from tests.pages.base_page import BasePage
from tests.pages.cart_page import CartPage
from tests.pages.login_page import LoginPage

class Navbar(BasePage):
    ACCOUNT_BTN_SELECTOR = (By.CSS_SELECTOR, 'a.single-icon[href="https://www.periplus.com/account/Your-Account"]')
    SEARCH_ID = (By.ID, "filter_name")
    CART_BTN_SELECTOR = (By.CSS_SELECTOR, 'a.single-icon[href="https://www.periplus.com/checkout/cart"]')

    def click_account_button(self): 
        self.wait_for_preloader()
        account_btn = self.driver.find_element(*self.ACCOUNT_BTN_SELECTOR)
        self.driver.execute_script("arguments[0].click();", account_btn)
        return LoginPage(self.driver)
    
    def search_product(self, product_name):
        self.wait_for_preloader()
        search_box = self.driver.find_element(*self.SEARCH_ID)
        search_box.send_keys(product_name + Keys.RETURN)

    def click_cart_button(self):
        self.wait_for_preloader()
        cart_btn = self.driver.find_element(*self.CART_BTN_SELECTOR)
        self.driver.execute_script("arguments[0].click();", cart_btn)
        return CartPage(self.driver)