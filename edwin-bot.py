from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver import ActionChains

import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

from edwinFunctions.pageChecks import readyCheck
from edwinFunctions.pageLogin import edwinLogin, edwinOrientate, edwinSecrets


if __name__ == "__main__":
    
    print('Starting bot...')
    driver = webdriver.Chrome('chromedriver')

    THIS_MONTH, THIS_MONTH_NUMERIC, LAST_MONTH, THIS_YEAR = edwinOrientate()
    LOGIN_LINK, BILLING_LINK, SETTINGS_LINK, USERNAME, PASSWORD = edwinSecrets()
    edwinLogin(driver, LOGIN_LINK, USERNAME, PASSWORD)


# DONE: Implement unit switching, check for gempa and sinaran!
# TODO: __main__ implementation 
# TODO: Cleanup with functions >> hide away and imports
# TODO: report both units together
# TODO: close webdriver at end of session
# TODO: keep log of costs