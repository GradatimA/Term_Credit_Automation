import time
from this import s

import pytest
from _pytest import mark
from selenium import webdriver
from pytest import fixture
from selenium.webdriver.firefox import options


@fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.implicitly_wait(10)
    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):
    return parser.addoption("--browser",action="store")



@fixture()
def browser(request):
    return request.config.getoption("--browser")

# Pytest Html reports

def pytest_configure(config):
    config._metadata = {
        "Tester": "Ganesan K",
        "Project Name": "ABSLI ",
        "Module Name" : "CLIORG creation"

    }


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)



