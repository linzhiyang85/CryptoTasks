from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):
    ### Locators ###
    ACCEPT_COOKIE = (By.XPATH, '//button[text()="Accept Cookies"]')
    ### END Locators ###

    def __init__(self, driver:WebDriver, wait_timeout=30):
        self.driver = driver
        self.waiter = WebDriverWait(driver, wait_timeout)

    def open(self, url):
        self.driver.get(url)

    def accept_cookie(self):
        if self.exists(self.ACCEPT_COOKIE):
            self.js_click(self.get_element(self.ACCEPT_COOKIE))

    def maximize_window(self):
        self.driver.maximize_window()

    def set_timeout(self, wait_timeout):
        self.waiter = WebDriverWait(self.driver, wait_timeout)

    def wait_for_existance(self, locator):
        self.waiter.until(EC.presence_of_element_located(locator))

    def wait_for_appear(self, locator):
        self.waiter.until(EC.visibility_of_element_located(locator))

    def wait_for_disappear(self, locator):
        self.waiter.until(EC.invisibility_of_element_located(locator))

    def wait_for_url_change(self, original_url):
        self.waiter.until(EC.url_changes(original_url))

    def exists(self, locator):
        try:
            self.wait_for_existance(locator)
            return True
        except Exception as ex:
            return False

    def get_element(self, locator):
        self.wait_for_existance(locator)
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        self.wait_for_existance(locator)
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        return self.get_element(locator).text

    def scroll_to_element(self, web_element):
        self.driver.execute_script('return arguments[0].scrollIntoView();', web_element)

    def scroll_half_screen_down(self):
        self.driver.execute_script(r'window.scrollBy(0, -window.innerHeight/2)')

    def click(self, locator):
        self.get_element(locator).click()

    def js_click(self, web_element):
        self.driver.execute_script('arguments[0].click();', web_element)

    def send_keys(self, locator, value):
        self.get_element(locator).send_keys(value)