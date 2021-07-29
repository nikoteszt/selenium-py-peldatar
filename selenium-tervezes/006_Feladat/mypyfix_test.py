import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope='session')
def brovser():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/alert_playground.html")
    return driver


def test_alert(browser):
    alert_button = browser.find_element_by_xpath('//input[@name="alert"]')
    alert_button.click()
    alert = browser.switch_to.alert
    assert (alert.text == "I am alert")
    time.sleep(1)
    alert.accept()
    time.sleep(1)
    assert ("Practice Alerts" in browser.page_source)


def test_confirmation(browser):
    confirmation_button = browser.find_element_by_xpath('//input[@name="confirmation"]')
    confirmation_button.click()
    alert = browser.switch_to.alert
    assert (alert.text == "I am confirm")
    time.sleep(1)
    alert.accept()
    time.sleep(1)
    assert ("Practice Alerts" in browser.page_source)


def test_prompt(browser):
    prompt_button = browser.find_element_by_xpath('//input[@name="prompt"]')
    prompt_button.click()
    alert = browser.switch_to.alert
    assert (alert.text == "I am prompt")
    alert.send_keys("Beirunk")
    time.sleep(1)
    alert.accept()
    time.sleep(1)
    assert ("Beirunk" in browser.find_element_by_xpath('//p[@id="demo"]').text)


def test_double_click(browser):
    double_click_button = browser.find_element_by_xpath('//input[@id="double-click"]')
    action = ActionChains(browser)
    action.double_click(double_click_button).perform()
    time.sleep(1)
    alert = browser.switch_to.alert
    assert (alert.text == "You double clicked me!!!, You got to be kidding me")
    time.sleep(1)
    alert.accept()
    time.sleep(1)
