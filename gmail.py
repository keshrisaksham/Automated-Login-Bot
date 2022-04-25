from selenium.webdriver.common.by import By
import constants

def fetch(driver):

        # fetching th gmail link
        driver.get(constants.GMAIL)
        driver.implicitly_wait(15)
        
        # finding the email fields and next button.
        mail_field = driver.find_element(By.XPATH, '//input[@id="identifierId"]')
        mail_field.send_keys(constants.EMAIL)
        next = driver.find_elements(By.XPATH, '//button/span')
        for items in next:
            if items.text != 'Next':
                continue
            items.click()
            break

        # finding the password fields and next button.
        passkey = driver.find_element(By.NAME, 'password')
        passkey.send_keys(constants.CREDS)
        next = driver.find_elements(By.XPATH, '//button/span')
        for items in next:
            if items.text != 'Next':
                continue
            items.click()
            break