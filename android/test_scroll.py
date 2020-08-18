import pytest
from time import sleep

@pytest.mark.usefixtures('setup')
class TestScroll():

    def test_scroll(self):
        sleep(3)
        for _ in xrange(15):
            print _
            end_y = 1200
            try:
                value = self.driver.find_element_by_id("my_site_blog_posts_text_view").is_displayed()
                if value is True:
                    break
            except:
                self.driver.swipe(417, 1400, 470, end_y, 300)
                self.driver.implicitly_wait(2)
                continue
            sleep(5)












