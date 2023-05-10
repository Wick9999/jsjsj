from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# Set up the Selenium WebDriver with the Chrome browser
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)

def vote():
    try:
        # Navigate to the top.gg voting page for your desired bot
        driver.get("https://top.gg/bot/<bot-id>/vote")

        # Find the vote button and click it
        vote_button = driver.find_element_by_xpath("//button[contains(text(), 'Vote')]")
        vote_button.click()

        # Wait for the page to load and verify that the vote was successful
        time.sleep(5)
        assert "Voted" in driver.page_source

        # Print success message
        print("Vote successful!")
    except Exception as e:
        print(e)

while True:
    # Call the vote function
    vote()

    # Wait for 12 hours before voting again
    time.sleep(12 * 60 * 60)
