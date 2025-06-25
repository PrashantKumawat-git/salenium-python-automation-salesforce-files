import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestToVerifyAgeOnCase:
    try:
        def createCase(self, driver, rsdate, age):
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Case/list?filterName=__Recent")
            print("\nClick on the Cases tab")
            driver.find_element(By.XPATH, "//div[@title='New']").click()
            print("Click on the New button")
            driver.find_element(By.XPATH, "//label[@for='012J4000000kF5cIAE']// span[@class='slds-radio--faux']").click()
            print("Select Inquery record type")
            driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
            print("Click on Next")
            driver.find_element(By.XPATH, "//button[@aria-label='Case Origin']").click()
            print("Click on Case Origin Picklist")
            driver.find_element(By.XPATH, "//div[@aria-label='Case Origin']// span[@title='Web']").click()
            print("Select Web")
            driver.find_element(By.XPATH, "//input[@placeholder='Search Contacts...']").send_keys("New")
            print("Search for Contacts in lookup")
            driver.find_element(By.XPATH, "//lightning-base-combobox-item[@data-value='003J400000KMw5gIAD']").click()
            print("Select Contact")
            driver.find_element(By.XPATH, "//input[@placeholder='Search Accounts...']").send_keys("G")
            print("Search for Accounts in lookup")
            driver.find_element(By.XPATH, "//lightning-base-combobox-item[@data-value='001J400000WkQHnIAN']").click()
            print("Select Account")
            driver.find_element(By.XPATH, "//input[@name='Resolution_Date__c']").send_keys(rsdate)
            print("Fill Resolution Date as:"+rsdate)
            driver.find_element(By.XPATH, "//input[@name='Subject']").send_keys("New Case for Testing")
            print("Fill Subject as: New Case for Testing")
            driver.find_element(By.XPATH, "//input[@name='Age__c']").send_keys(str(age))
            print("Fill age as: "+ str(age))

        def test01_create_case_with_valid_age(self, browser):
            print("executing test01_create_case_with_valid_age")
            self.createCase(browser, "25/05/2025", 18)
            browser.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Click on Save")

            wait = WebDriverWait(browser, 10)
            case_number_element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                               "//span[text()='Case Number']/ancestor::div[contains(@class,'slds-form-element')]//lightning-formatted-text")))
            case_number = case_number_element.text

            print(f"The Case Number is: " + str(case_number))
            assert case_number.isdigit()

        def test02_create_case_with_invalid_age(self, browser):
            print("executing test02_create_case_with_valid_age")
            self.createCase(browser, "25/05/2025", 16)
            browser.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Click on Save")
            time.sleep(4)
            try:
                validation_msg = "Age must be 18 or greater. Please enter a valid value."
                error_text = browser.find_element(By.XPATH,
                                                  "//div[contains(@class, 'form-element__help') and contains(text(), 'Age must')]").text
                lines = error_text.strip().split('\n')
                actual_error = lines[-1]
                print(f"Validation Error: {actual_error}")
                #error_msg = browser.find_element(By.XPATH, "//div[@data-name='Age__c']").text
                #print(error_msg)
                assert validation_msg in error_text
            except NoSuchElementException:
                pytest.fail("Validation error not found")

        def test03_force_assertion_fail_case(self, browser):
            print("executing test03_create_case_with_valid_age")
            self.createCase(browser, "25/05/2025", 10)
            browser.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Click on Save")
            time.sleep(4)

            validation_msg = "Age must be 18 or greater. Please enter a valid value."
            error_text = browser.find_element(By.XPATH,
                                                  "//div[contains(@class, 'form-element__help') and contains(text(), 'Age must')]").text
            lines = error_text.strip().split('\n')
            actual_error = lines[-1]
            print(f"Validation Error: {actual_error}")
            try:
                if validation_msg == error_text:
                    print("Assertion Passed")
                else:
                    print("Assertion Failed")
            except NoSuchElementException:
                pytest.fail("Validation error not found")

            assert validation_msg == error_text, f"Assertion Failed: Expected '{validation_msg}' but got '{error_text}'"


    except Exception as e:
        print(e)
    finally:
        print("Exit from the class")