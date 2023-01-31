from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class SearchResultsPage(PageFactory):

    GOOGLE_DEFAULT_LINKS = ['https://webcache.googleusercontent.com/',
                            'https://translate.google.com/',
                            'https://www.google.com/search']

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "found_links": ("XPATH", '//*[@id="rso"]/div//a')
    }

    def get_all_links(self):
        found_links = self.driver.find_elements(By.XPATH, self.locators["found_links"][1])
        return [link.get_attribute('href') for link in found_links]

    def remove_default_google_links(self, list):
        return [str for str in list if not any(sub in str for sub in self.GOOGLE_DEFAULT_LINKS)]

    def get_links_which_contain(self, substring):
        found_links = self.remove_default_google_links(self.get_all_links())
        return [link for link in found_links if substring in link]

