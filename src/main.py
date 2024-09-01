from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login import login_to_home


def main():
    # Define Browser
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    # login
    browser = login_to_home(browser=browser)


main()
