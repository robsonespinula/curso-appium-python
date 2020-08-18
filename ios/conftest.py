import os
import pytest
from appium import webdriver

@pytest.fixture(scope='class')
def setup(request):
    app = os.path.abspath(
        '/Users/robsons/Library/Developer/Xcode/DerivedData/WordPress-gwcecnedfdbgxzehsyzvpfckumnp/Build/Products/Debug-iphonesimulator/WordPress.app')
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                   desired_capabilities={
                                       'app': app,
                                       'platformName': 'iOS',
                                       'platformVersion': '13.3',
                                       'deviceName': 'iPhone 8',
                                       'noReset': 'True',
                                   })
    request.cls.driver = driver
    yield
    driver.quit()