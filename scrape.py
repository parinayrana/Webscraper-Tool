from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup


def scrape_website(website):
    print("Launching chrome browser...")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options= options)

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(0)

        return html
    finally:
        driver.quit()
    

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

