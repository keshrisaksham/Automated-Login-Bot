from selenium.webdriver.common.by import By
import constants

def fetch(driver):

        # fetching the facebook link.
        driver.get(constants.FACEBOOK_LINK)                                                                                       
        driver.implicitly_wait(15)
    
        # finding the mail and password input field and putting the email and password.
        mail_field = driver.find_element(By.NAME, "email")
        mail_field.send_keys(constants.EMAIL)
        passkey = driver.find_element(By.NAME, "pass")
        passkey.send_keys(constants.CREDS)
    
        # clicking on the login button
        login = driver.find_element(By.NAME, 'login')
        login.click()
