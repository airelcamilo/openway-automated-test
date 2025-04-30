from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage  

class CartPage(BasePage):
    CART_ITEM_SELECTOR = (By.CSS_SELECTOR, ".row.row-cart-product")
    CART_ITEM_NAME_SELECTOR = (By.CSS_SELECTOR, ".product-name.limit-lines > a")
    CART_ITEM_ISBN_SELECTOR = (By.CSS_SELECTOR, "div.row")
    CART_ITEM_QUANTITY_SELECTOR = (By.CSS_SELECTOR, "input.input-number")

    def cart_items(self):
        self.wait_for_preloader()
        return self.driver.find_elements(*self.CART_ITEM_SELECTOR)
    
    def get_cart_item_name(self, cart_item):
        return cart_item.find_element(*self.CART_ITEM_NAME_SELECTOR)
    
    def get_cart_item_isbn(self, cart_item):
        return cart_item.find_elements(*self.CART_ITEM_ISBN_SELECTOR)[2]
    
    def get_cart_item_quantity(self, cart_item):
        return cart_item.find_element(*self.CART_ITEM_QUANTITY_SELECTOR)