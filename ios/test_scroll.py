import pytest
from time import sleep

@pytest.mark.usefixtures('setup')
class TestScroll():

    def test_scroll(self):
        el = self.driver.find_element_by_accessibility_id("Blog Posts")
        self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
        sleep(2)
        self.driver.find_element_by_accessibility_id("Blog Posts").click()