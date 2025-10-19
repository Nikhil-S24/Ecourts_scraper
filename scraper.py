# scraper.py
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def download_cause_lists(download_folder="Cause_Lists"):
    """
    Navigates to the specified court website, finds all PDF links,
    and downloads them into a folder.
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # The URL from the task clarification
    url = 'https://newdelhi.dcourts.gov.in/cause-list-%e2%81%84-daily-board/'

    # This automatically sets up and launches a Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Go to the website
        driver.get(url)
        # Wait a few seconds for everything to load
        time.sleep(3) 

        # Parse the page's HTML to find all links
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        pdf_links = [link['href'] for link in soup.find_all('a', href=True) if ".pdf" in link['href']]

        if not pdf_links:
            return "No PDF cause lists were found on the page."

        # Loop through each link and download the file
        for pdf_url in pdf_links:
            file_name = os.path.join(download_folder, pdf_url.split('/')[-1])
            try:
                response = requests.get(pdf_url)
                with open(file_name, 'wb') as f:
                    f.write(response.content)
            except Exception as e:
                print(f"Could not download {pdf_url}. Error: {e}")

        return f"Success! Downloaded {len(pdf_links)} PDF files to the '{download_folder}' folder."

    finally:
        # Always close the browser when done
        driver.quit()