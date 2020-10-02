#Conftest.py file is used in pytest framework for accessing all the common function that can be used through the project
# without any imports.

import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Drivers.Chromedriver import driver
from Pages.Locators import signin, signout


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def pretest(request):
    login_page()
    login()
    yield driver
    if request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            screenshot(request)
        else:
            print("Test execution completed succesfully")
    logout()


@pytest.fixture(scope="session", autouse=True)
def posttest(request):
    yield driver
    driver.quit()



def login_page():
    test_site = "http://automationpractice.com/index.php"
    driver.get(test_site)


def login():
    username = "shankar_ud@outlook.com"
    password = "1234567890"
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(signin.Tab_signin).click()
    driver.implicitly_wait(20)
    driver.find_element_by_id(signin.txt_email).send_keys(username)
    driver.find_element_by_id(signin.txt_password).send_keys(password)
    driver.find_element_by_id(signin.Btn_signin).click()


def logout():
    wait = WebDriverWait(driver, 200)
    wait.until(EC.element_to_be_clickable((By.XPATH, signout.Tab_logout)))
    driver.find_element_by_xpath(signout.Tab_logout).click()


def screenshot(request):
    label = str(request.node.name)
    path = "../Source/Screenshots/" + label + "_" + names() + ".png"
    driver.save_screenshot(path)


def names():
    date = str(datetime.now().date())
    now = datetime.now()                                                        # to return random names with timestamp
    temp = ('%02d%02d%d' % (now.minute, now.second, now.microsecond))[:-4]
    name = str(date+temp)
    return name