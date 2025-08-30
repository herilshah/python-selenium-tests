from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins CI/CD")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)  # wait for search results to load

    assert "Jenkins" in driver.title

    driver.quit()
