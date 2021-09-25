from page.base import BasePage
from selenium.webdriver.common.by import By
class ExchangePage(BasePage):
    ### locators ###
    MARKET_MENU_ITEMS = (By.CSS_SELECTOR, '.market-title-box .e-tabs__nav-item')
    INSTRUMENT_NAMES = (By.CSS_SELECTOR, '.trade-list .instrument-name')
    ### END locators ###

    def click_market_menu(self, item_name):
        items = self.get_elements(self.MARKET_MENU_ITEMS)
        for item in items:
            if item.text == item_name:
                self.scroll_to_element(item)
                item.click()

    def get_active_market_menu(self):
        items = self.get_elements(self.MARKET_MENU_ITEMS)
        for item in items:
            if 'active' in item.get_attribute('class'):
                return item.text
        return None

    def get_instrument(self, source, target):
        instruments = self.get_elements(self.INSTRUMENT_NAMES)
        for instrument in instruments:
            if instrument.find_element_by_class_name('source').text == source and \
               instrument.find_element_by_class_name('target').text.replace('/', '') == target:
                return instrument
        return None

    def open_instrument(self, instrument):
        self.scroll_to_element(instrument)
        self.scroll_half_screen_down()

        trade_button = instrument.find_elements_by_xpath('./ancestor::tr//button[text()="Trade"]')
        if len(trade_button) > 0:
            try:
                trade_button[0].click()
            except:
                instrument.click()
        else:
            instrument.click()
