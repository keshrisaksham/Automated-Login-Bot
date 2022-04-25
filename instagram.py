from selenium.webdriver.common.by import By
import constants

def fetch(driver):
        
        # fetching the instagra link
        driver.get(constants.INSTAGRAM_LINK)
        driver.implicitly_wait(15)
        
        # finding the email and password fields
        mail_field = driver.find_element(By.XPATH, '//input[@name= "username"]')
        mail_field.send_keys(constants.EMAIL)
        passkey = driver.find_element(By.XPATH, '//input[@name= "password"]')
        passkey.send_keys(constants.CREDS)

        # clicking on the login button
        login = driver.find_element(By.XPATH, '//button[@type = "submit"]')
        login.click()
        
        # disable the save password pop-up, its completely optional. 
        driver.find_element(By.XPATH, '//div[@class="cmbtv"]/button').click()
