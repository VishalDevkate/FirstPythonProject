import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture(params=["chrome", "edge"])
@pytest.fixture(scope="package")
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"creating {browser} driver")
    if browser == "chrome":
        # my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        my_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Invalid value for argument --browser. Expected edge, chrome or firefox, but got {browser}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    print(f"closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge", help="browser for execution: chrome or firefox"
    )
