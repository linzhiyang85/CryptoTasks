import pytest
from selenium.webdriver import Chrome, Firefox
import os
from common.configHelper import Config

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="e2e",
        help="run test cases in which environment"
    )

    parser.addoption(
        "--browser", action="store", default="chrome",
        help="run test cases in which environment"
    )

@pytest.fixture(scope='session')
def env(pytestconfig):
    return pytestconfig.getoption('--env').lower()

@pytest.fixture(scope='session')
def browser(pytestconfig):
    return pytestconfig.getoption('--browser').lower()

@pytest.fixture(scope='session')
def settings(env):
    return Config(env)

@pytest.fixture
def driver(browser):
    if browser == 'chrome':
        driver = Chrome(executable_path=os.path.join('driver', 'chromedriver.exe'))
    elif browser == 'firefox':
        driver = Firefox()
    else:
        driver = None
    assert driver is not None, 'Failed to initialize browser'

    yield driver
    driver.quit()