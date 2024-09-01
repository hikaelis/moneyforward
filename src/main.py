from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login import login_to_home
from pages import get_page
from line_message import send_text_message


def main():
    # Define Browser
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    # login
    browser = login_to_home(browser=browser)

    # '資産'ページに移動
    asset_page = get_page(browser=browser, target_page="asset")


main()
