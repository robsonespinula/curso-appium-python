import pytest
from time import sleep

@pytest.mark.usefixtures('setup')
class TestLogin():

    def test_login(self):

        self.driver.find_element_by_accessibility_id('Prologue Log In Button').click()
        self.driver.find_element_by_accessibility_id('Log in with Email Button').click()
        self.driver.find_element_by_accessibility_id('Login Email Address').send_keys('robsonespinula@gmail.com')
        self.driver.find_element_by_accessibility_id('Login Email Next Button').click()
        sleep(5)
        self.driver.find_element_by_accessibility_id('Use Password').click()
        sleep(5)
        self.driver.find_element_by_accessibility_id('Password').send_keys('rse91160028')
        self.driver.find_element_by_accessibility_id('Password Next Button').click()









