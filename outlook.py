from selenium.webdriver.common.by import By
import constants
import time

def fetch(driver):

    #visiting outlook.com
    driver.get(constants.OUTLOOK_LINK)
    #clicking signin button
    driver.find_element(By.XPATH, '//nav/ul/li[2]/a').click()

    #finding the input field and puting the mail and then clicking next.
    driver.find_element(By.ID, 'i0116').send_keys(constants.EMAIL)
    driver.find_element(By.ID, 'idSIButton9').click()

    #Finding password field and putting the password and then clicking next.
    driver.find_element(By.ID, 'i0118').send_keys(constants.CREDS)
    time.sleep(2)
    driver.find_element(By.ID, 'idSIButton9').click()

    try:
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
    except:
        print ('Logged in.\nIt did not ask to save the creds.')
