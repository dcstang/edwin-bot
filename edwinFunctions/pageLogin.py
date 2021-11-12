import os
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from dotenv import load_dotenv

from .pageChecks import readyCheck


def edwinSecrets():
    load_dotenv()

    LOGIN_LINK = os.environ.get('LOGIN_LINK')
    BILLING_LINK = os.environ.get('BILLING_LINK')
    SETTINGS_LINK = os.environ.get('SETTINGS_LINK')

    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')

    return LOGIN_LINK, BILLING_LINK, SETTINGS_LINK, USERNAME, PASSWORD

def edwinLogin(driver, LOGIN_LINK, USERNAME, PASSWORD): 
    """Login on page using secrets from .env

    Args:
        driver (selenium object): declared Webdriver/Chromium, etc
        LOGIN_LINK (string): loaded in from .env
        USERNAME (string): secret loaded in from .env
        PASSWORD (string): secret loaded in from .env
    """
    driver.get(LOGIN_LINK)
    readyCheck(driver)

    driver.find_element(By.NAME, 'username').send_keys(USERNAME)
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)

    # login button click - need to generalise later
    driver.find_element(By.CLASS_NAME, 'btn-lg').click()
    readyCheck(driver)

    print('Login successful')

def edwinOrientate():
    THIS_MONTH = datetime.today().strftime('%b')
    THIS_MONTH_NUMERIC = datetime.today().strftime('%m')
    LAST_MONTH = (datetime.today() - timedelta(days=20)).strftime('%b')
    THIS_YEAR = datetime.today().strftime('%Y')

    return THIS_MONTH, THIS_MONTH_NUMERIC, LAST_MONTH, THIS_YEAR