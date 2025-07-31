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

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser" )

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()   #getting rid of the style and script tags 

    cleaned_content = soup.get_text(separator="\n")  #getting all of the text and separating it by a new line
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())  # to remove empty strings

    return cleaned_content
