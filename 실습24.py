from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import keys

cp = chromedriver_autoinstaller
browser = webdriver.Chrome(cp)
browser.get("https://www.youtube.com/watch?v=awGwP7Z_ROw")
time.sleep(5)