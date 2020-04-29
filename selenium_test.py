#code to initialize driver location
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add = "/Users/priyanshbendre/Priyansh/selenium_drivers/chromedriver"
driver = webdriver.Chrome(chrome_options=options, executable_path="/Users/priyanshbendre/Priyansh/selenium_drivers/chromedriver")

driver.get("https://google.com")
