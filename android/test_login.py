import pytest
from time import sleep

@pytest.mark.usefixtures('setup')
class TestLogin():
    def test_login(self):
        self.driver.find_element_by_id("login_button").click()
        sleep(2)
        self.driver.find_element_by_id("input").send_keys('robsonespinula@gmail.com')
        self.driver.find_element_by_id("primary_button").click()
        sleep(5)
        self.driver.find_element_by_id("login_enter_password").click()
        sleep(2)
        self.driver.find_element_by_id("input").send_keys('rse91160028')
        self.driver.find_element_by_id("primary_button").click()

