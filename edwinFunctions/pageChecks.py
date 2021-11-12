from selenium.webdriver.support.ui import WebDriverWait

# helper functions
def readyCheck(driver):
    """Check if page is fully loaded before proceeding to next step

    Returns:
        boolean: True (once page is loaded)
    """
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    return True