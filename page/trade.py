from page.base import BasePage
from selenium.webdriver.common.by import By

class TradePage(BasePage):
    ### locators ###
    INSTRUMENT_TOGGLE = (By.CSS_SELECTOR, '.symbol-info .toggle')
    ### END locators ###

    def get_instrument_name(self):
        return self.get_text(self.INSTRUMENT_TOGGLE).strip()
