import os
import pytest
from appium import webdriver

@pytest.fixture(scope='class')
def setup(request):
    app = os.path.abspath('/Users/robsons/Downloads/Android/WordPress.apk')
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                   desired_capabilities={
                                       'app': app,
                                       'platformName': 'Android',
                                       'platformVersion': '8.1.0',
                                       'deviceName': 'android',
                                       'appPackage': 'org.wordpress.android',
                                       'appActivity': 'org.wordpress.android.ui.WPLaunchActivity',
                                       'noReset': 'True',
                                   })
    request.cls.driver = driver
    yield
    driver.quit()