import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1400
    browser.config.window_height = 800
    browser.config.base_url = 'https://demoqa.com'

    yield
    browser.quit()