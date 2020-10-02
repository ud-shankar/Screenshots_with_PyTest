from Drivers.Chromedriver import driver
import pytest
from pytest_bdd import scenario, given, when, then
from Pages.Locators import signin, homepage


# @pytest.mark.practice          # Used to run in the terminal using command pytest -m login
# @scenario('../Features/Automation_practice.feature', 'User is trying to Login using the username and password textbox')
# def test_login_page():
#     pass


@pytest.mark.practice          # Used to run in the terminal using command pytest -m login
@scenario('../Features/Automation_practice.feature', 'User is trying to click on my address with incorrect locator (Auto screenshot feature)')
def test_screenshot():
    pass


@given("User opens login in page")
def logging_in():
    pass # WE use pretest fuction in Conftest.py file with autouse markup true for every function


@when("User enters username and password and clicks sign-in button")
def username_password():
    pass  # WE use pretest fuction in Conftest.py file with autouse markup true for every function


@when("User is in Home page")
def assert_homepage():
    driver.implicitly_wait(20)
    assert driver.find_element_by_xpath(signin.loggedin_name).is_displayed()


@then("User is logged-in")
def logout():
    pass # WE use pretest fuction in Conftest.py file with autouse markup true for every function


@then("User clicks on My address with incorrect locator and screenshot is captured")
def failed_test():
    driver.find_element_by_id(homepage.My_address).click()
