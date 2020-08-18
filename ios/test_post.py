import pytest
from time import sleep

@pytest.mark.usefixtures('setup')
class TestPost():

    def test_post(self):
        el = self.driver.find_element_by_accessibility_id("Blog Posts")
        self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
        sleep(2)
        self.driver.find_element_by_accessibility_id("Blog Posts").click()
        self.driver.find_element_by_accessibility_id("Add").click()
        sleep(3)
        self.driver.find_element_by_accessibility_id("Add title").send_keys("Post Teste")
        self.driver.find_element_by_accessibility_id("add-block-button").click()
        self.driver.find_element_by_accessibility_id("Image").click()


