import pytest

from ui_tests.page_objects.scores_page import ScoresPage
from ui_tests.page_objects.search_page import SearchPage


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    def go_to(self, url):
        self.driver.get(url)
        return self.driver


class TestLiveScoreSearch(BasicTest):
    def test_open_url(self):
        """
        Check search of livescore on Google and open links
        """
        search_results_page = SearchPage(self.driver) \
            .accept_all_cookies() \
            .type_search_request("Livescore in israel") \
            .submit_search()

        livescore_links = search_results_page.get_links_which_contain('365scores')

        assert len(livescore_links) >= 1, "Found links must contain 365scores website, but found these results " \
                                          + str(search_results_page.get_all_links())

        for link in livescore_links:
            scores_page = ScoresPage(self.go_to(link))

            assert scores_page.get_title().is_displayed(), "Title must be visible on page " + link
