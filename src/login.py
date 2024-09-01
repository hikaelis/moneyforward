from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import os


def login_to_home(browser: webdriver.Chrome) -> webdriver.Chrome:
    """ログインしてトップページを取得する"""
    EMAIL = os.environ["EMAIL"]
    PASSWORD = os.environ["PASSWORD"]

    print("start login")

    # Jump to email sing-in page
    url = "https://ssnb.x.moneyforward.com/users/sign_in"
    browser.get(url)
    sleep(1)

    # Enter email
    elem_email = browser.find_element(
        by=By.XPATH,
        value='//*[@id="sign_in_session_service_email"]',
    )
    elem_email.send_keys(EMAIL)
    sleep(1)

    # Enter password
    elem_password = browser.find_element(
        by=By.XPATH,
        value='//*[@id="sign_in_session_service_password"]',
    )
    elem_password.send_keys(PASSWORD)
    sleep(1)

    # Click login
    elem_login2 = browser.find_element(
        by=By.XPATH,
        value='//*[@id="login-btn-sumit"]',
    )
    elem_login2.click()
    sleep(1)

    return browser
