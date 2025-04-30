from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys

from tests.pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, email, password):
        self.wait_for_element((By.NAME, "email")).send_keys(email) 
        self.wait_for_element((By.NAME, "password")).send_keys(password + Keys.RETURN)