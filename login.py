from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import constants
import facebook
import instagram
import twitter
import gmail
import outlook

serv = Service(constants.DRIVER_PATH_WIN)
driver = webdriver.Chrome(service = serv)
driver.maximize_window()

# facebook.fetch(driver)
# instagram.fetch(driver)
# twitter.fetch(driver)

# gmail.fetch(driver)
outlook.fetch(driver)