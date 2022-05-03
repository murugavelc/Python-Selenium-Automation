import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

# from utilities.customLogger import LogGen

@pytest.fixture()
def setup(browser):
    # logger = LogGen.logger()

    if browser == 'chrome':
        # service = ChromeService(executable_path=ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service)
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        # logger.info("========== Lunching Chrome browser ===========")
    elif browser == 'firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        # logger.info("========== Lunching Firefox browser ===========")
    elif browser == 'edge':
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        # logger.info("========== Lunching Edge browser ===========")
    elif browser == "ie":
        service = IEService(executable_path=IEDriverManager().install())
        driver = webdriver.Ie(service=service)
        # logger.info("========== Lunching IE browser ===========")
    else:  # Make default browser if CLI is not passed
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # service = ChromeService(executable_path="D
        # :/python/automation/selenium/webdriver/chromedriver.exc")
        # driver = webdriver.Chrome(service=service)

    return driver


def pytest_addoption(parser):  # This will get value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")

# PyTest HTML Report
def pytest_configure(config):  # This is hook for adding environment info in HTML report
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester Name'] = 'Murugavel C'


@pytest.mark.optionalhook
def pytest_metadata(metadata):  # This hook for delete/modify environment info in HTML report
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)


