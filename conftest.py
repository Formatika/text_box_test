import pytest
from selenium import webdriver

@pytest.fixture(scope="class", params=["chrome"])
def browser(request):
    browser_name = request.param
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
    elif browser_name == "firefox": #Пример подключения firefox
        options = webdriver.FirefoxOptions()
        options.set_preference("detach", True)

    else:
        raise ValueError(f"Invalid browser name: {browser_name}. Please use 'chrome' or 'firefox'.")
    browser = webdriver.Remote(command_executor="http://192.168.0.5:4444/wd/hub", options=options)

    browser.maximize_window()
    yield browser
    browser.quit()



