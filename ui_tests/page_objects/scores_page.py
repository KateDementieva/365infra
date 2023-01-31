from selenium.webdriver import ActionChains
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.keys import Keys

from ui_tests.page_objects.search_results_page import SearchResultsPage


class ScoresPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "title": ("CSS", 'div[class*=all-scores-widget_container]  h2'),
        "submit_btn": ("CSS", 'body center > input[name="btnK"]'),
        "accept_all": ("XPATH", "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div")
    }

    def get_title(self):
        return self.title

    def type_search_request(self, search_string):
        self.search_bar.set_text(search_string)
        return self

    def submit_search(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        return SearchResultsPage(self.driver)
