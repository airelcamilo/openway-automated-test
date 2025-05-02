import os
from dotenv import load_dotenv

from tests.pages.home_page import HomePage
from tests.pages.navbar import Navbar

load_dotenv()
EMAIL = os.getenv("PERIPLUS_EMAIL")
PASSWORD = os.getenv("PERIPLUS_PASSWORD")

def test_add_product_to_cart(driver):
    assert EMAIL is not None, "EMAIL is not loaded from .env"
    assert PASSWORD is not None, "PASSWORD is not loaded from .env"

    # Navigates to https://www.periplus.com/
    home_page = HomePage(driver)
    home_page.open_page()
    navbar = Navbar(driver)
    
    # Go to login page and enter email and password
    login_page = navbar.click_account_button()
    login_page.login(EMAIL, PASSWORD)

    # Find one product
    navbar.search_product("Children Of Time Adrian")
    detail_page = home_page.open_product_detail_by_index(0)

    # Add the product to the cart
    product_name = detail_page.get_product_name()
    product_isbn = detail_page.get_product_isbn()
    detail_page.click_add_to_cart_button()

    # Go to cart page and verify the product has been successfully added to the cart
    cart_page = navbar.click_cart_button()
    cart_items = cart_page.cart_items()
    cart_item = cart_items[0]
    
    assert cart_item is not None, "Product was not added to cart"

    cart_item_name = cart_page.get_cart_item_name(cart_item)
    assert cart_item_name.text.strip().lower() == product_name.lower()
    cart_item_isbn = cart_page.get_cart_item_isbn(cart_item)
    assert cart_item_isbn.text.strip() == product_isbn
    cart_item_quantity = cart_page.get_cart_item_quantity(cart_item)
    assert cart_item_quantity.get_attribute("value") == "1"

