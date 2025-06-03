import pytest
from selenium.webdriver.common.by import By
from datetime import datetime
import time

@pytest.mark.usefixtures("browser")
class TestVerifyContactOnCase:
    try:
        def test_create_account_and_verify_related_contact(self,browser):
            driver = browser
            # Click on Account tab to create Account record
            driver.find_element(By.XPATH, "//a[contains(text(),'Accounts')]").click()
            print("Click on Accounts tab")

            # Create a New Account record
            driver.find_element(By.XPATH, "//a[@title='New']").click()
            time.sleep(2)
            Name= "Test Automation Account "
            now = datetime.now().strftime("%Y%m%d%H%M%S")
            driver.find_element(By.XPATH, "//input[@name='Name']").send_keys(Name+str(now))
            driver.find_element(By.XPATH, "//label[text()='Rating']/following-sibling::div//button").click()
            driver.find_element(By.XPATH, "//span[@title='Hot']").click()
            driver.find_element(By.XPATH, "//input[@name='Phone']").send_keys("1234567890")
            driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Account record is created with Name,Rating and Phone fields")

            # Add related Contact of the above Account
            driver.find_element(By.XPATH, "//a[contains(@data-label, 'Related')]").click()
            print("click on Related tab")
            driver.find_element(By.XPATH, "//button[@name='NewContact']").click()
            print("Click on New Contact button from the Contacts Related list")
            driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys(str(now))
            print("Entered Last Name")
            driver.find_element(By.XPATH, "//input[@name='Title']").send_keys("Contact "+str(now))
            print("Entered Title")
            driver.find_element(By.XPATH, "//input[@name='Email']").send_keys("automation"+str(now)+"@testing.com")
            print("Entered Email")
            driver.find_element(By.XPATH, "//input[@name='Is_Primary__c']").click()
            print("Checked IsPrimary checkbox")
            driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Click on Save")
            time.sleep(3)

    except Exception as e:
        print(e)

    finally:
        print("Exit from the class")
