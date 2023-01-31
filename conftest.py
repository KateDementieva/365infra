import pytest
from selenium import webdriver

from environment import UI_BASE_URL


@pytest.fixture()
def driver_init(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    web_driver.get(UI_BASE_URL)
    web_driver.maximize_window()
    yield
    web_driver.close()
