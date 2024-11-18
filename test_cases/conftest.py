import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="specify the browser: chrome or firefox or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported Browser")
    return driver


####### for pytest html reports ########
# hooks for adding enevironment info in html repots

def pytest_configure(config):
    config.stash[metadata_key]['projectName'] = 'EcommerceProject,nop Commerce'
    config.stash[metadata_key]['TestModuleName'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'MAHESH'
    # hook for delete details from environment to html reports


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('PYTHON_HOME', None)
    metadata.pop('Plugins', None)
