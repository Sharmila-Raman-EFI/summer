import pytest
from selenium.webdriver import Chrome,Firefox,Ie

def get_browser_instance():

    browser_info= pytest.config.option.browser
    test_url_info= pytest.config.option.url
    if browser_info == "chrome":
        driver=Chrome("./Browser-Servers/chromedriver.exe")
    elif browser_info == "Firefox":
        driver=Firefox("./Browser-Servers/geckodriver.exe")
    elif browser_info == "Ie":
        driver=Ie("./Browser-Servers/IEDriverServer.exe")
    else:
        print("!!!!!!Invalid Browser option please check --browser parameter from CMD!!!!!!!!")
        return None

    driver.maximize_window()
    driver.implicitly_wait(30)
    if test_url_info == 'test':
        driver.get("https://tot.efi.com")
    elif test_url_info == 'prod':
        driver.get("https:// demo.actitime.com")
    return driver





