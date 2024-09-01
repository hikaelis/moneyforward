from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def get_page(browser: webdriver.Chrome, target_page: str) -> webdriver.Chrome:
    """各種ページを取得する"""
    value = ""
    if target_page == "top":
        value = '//*[@id="header-container"]/header/div[2]/ul/li[1]/a'
    elif target_page == "household":
        value = '//*[@id="header-container"]/header/div[2]/ul/li[2]/a'
    elif target_page == "budget":
        value = '//*[@id="header-container"]/header/div[2]/ul/li[3]/a'
    elif target_page == "asset":
        value = '//*[@id="header-container"]/header/div[2]/ul/li[4]/a'
    elif target_page == "analysis":
        value = '//*[@id="header-container"]/header/div[2]/ul/li[5]/a'
    elif target_page == "accounts":
        value = '//*[@id="header-container"]/header/div[2]/ul/li[6]/a'
    else:
        print("ページが存在しません")

    elem_target_page = browser.find_element(by=By.XPATH, value=value)
    elem_target_page.click()
    sleep(1)

    return browser
