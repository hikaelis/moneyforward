from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

# Define browser
options = webdriver.ChromeOptions()

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

print("start login")

# Jump to email sing-in page
url = "https://id.moneyforward.com/sign_in/email"
browser.get(url)
sleep(1)

# Enter email
elem_loginMethod = browser.find_element(
    by=By.XPATH,
    value="/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/input",
)
elem_loginMethod.send_keys(EMAIL)
sleep(1)

# Click login
elem_login1 = browser.find_element(
    by=By.XPATH,
    value="/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input",
)
elem_login1.click()
sleep(1)

# Enter password
elem_password = browser.find_element(
    by=By.XPATH,
    value="/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/input[2]",
)
elem_password.send_keys(PASSWORD)
sleep(1)

# Click login
elem_login2 = browser.find_element(
    by=By.XPATH,
    value="/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input",
)
elem_login2.click()
sleep(1)

# Click forwardme
elem_login3 = browser.find_element(
    by=By.XPATH, value="/html/body/main/div/div[2]/div/div[1]/div/ul/li[2]/a"
)
elem_login3.click()
sleep(1)

# Click login
elem_login4 = browser.find_element(
    by=By.XPATH,
    value="/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[2]/input",
)
elem_login4.click()
sleep(1)

# Click Group
elem_group = browser.find_element(
    by=By.XPATH, value='//*[@id="group_id_hash"]/option[3]'
)
elem_group.click()
sleep(1)

# 資産タブに移動
elem_portfolio = browser.find_element(
    by=By.XPATH, value='//*[@id="header-container"]/header/div[2]/ul/li[4]/a'
)
elem_portfolio.click()
sleep(1)
