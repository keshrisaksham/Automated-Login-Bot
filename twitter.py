from selenium.webdriver.common.by import By
import constants

def fetch(driver):

        # fetching twitter link
        driver.get(constants.TWITTER_LINK)
        driver.implicitly_wait(15)

        # finding the email field and the next button and then doing the required.
        mail_field = driver.find_element(By.XPATH, '//input[@type = "text"]')
        mail_field.send_keys(constants.EMAIL)
        next = driver.find_elements(By.XPATH, '//div[6]//span')
        for items in next:
            if items.text != 'Next': 
                continue
            items.click()
            break

        # finding the password field and the next button and then doing the required.
        passkey = driver.find_element(By.NAME, 'password')
        passkey.send_keys(constants.CREDS)
        next = driver.find_elements(By.XPATH, '//div/span/span')
        for items in next:
            if items.text != 'Log in':
                continue
            items.click()
            break