from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.geolocation": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.google.com/")

inputs = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi").send_keys("Web Developer")







