import sqlite3

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


@pytest.fixture
def session():
    connection = sqlite3.connect(':memory:')
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
def setup_db(session):
    session.execute('''CREATE TABLE users
                          (name text, active boolean)''')
    session.execute('INSERT INTO users VALUES ("John", 1)')
    session.connection.commit()
