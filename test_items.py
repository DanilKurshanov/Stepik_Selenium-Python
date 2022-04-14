from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


def test_find_button(browser, link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209/'):
    browser.get(link)
    time.sleep(15)

    assert WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-loading-text$="..."]'))), 'button not exists'
