import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(60)
    yield driver
    driver.quit()
