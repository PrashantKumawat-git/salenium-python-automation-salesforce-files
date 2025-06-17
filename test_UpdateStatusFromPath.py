import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
class TestVerifyContactOnCase:

    def test_create_contact(self,browser):
        driver = browser
        driver.implicitly_wait(20)

        try:
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Case/list?filterName=__Recent")
            print("Go to the Cases tab")

            driver.find_element(By.XPATH, "//div[@title='New']").click()
            print("Click on New button")

            driver.find_element(By.XPATH, "//label[@for='012J4000000kF5cIAE']// span[@class='slds-radio--faux']").click()
            print("Select Inquiry record type")

            driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
            print("Click on Next")

            driver.find_element(By.XPATH, "//button[@aria-label='Case Origin']").click()
            print("Click on Case Origin")

            driver.find_element(By.XPATH, "//div[@aria-label='Case Origin']// span[@title='Web']").click()
            print("Select Web")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Contacts...']").send_keys("New")
            print("Search for Contacts")

            driver.find_element(By.XPATH, "//div[@role='listbox']// lightning-base-combobox-item[@data-value='003J400000KMw5gIAD']").click()
            print("Contact selected")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Accounts...']").send_keys("G")
            driver.find_element(By.XPATH, "//div[@role='listbox']// lightning-base-combobox-item[@data-value='001J400000WkQHnIAN']").click()
            print("Account Selected")

            driver.find_element(By.XPATH, "//input[@name='Resolution_Date__c']").send_keys("25/05/2025")
            print("Selected Resolution Date as : 25/05/2025")
            driver.find_element(By.XPATH, "//input[@name='Subject']").send_keys("New Case for Testing")
            print("Entered Subject as : New Case for Testing")
            driver.find_element(By.XPATH, "//input[@name='Age__c']").send_keys("40")
            print("Entered age as : 18")
            driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Click On Save")
            print("Case is Created")
            time.sleep(3)

            case_number = driver.find_element(By.XPATH, "//span[text()='Case Number']/ancestor::div[contains(@class,'slds-form-element')]//lightning-formatted-text").text
            print("The Case Number is: " + str(case_number))

            status = driver.find_element(By.XPATH, "//a[@title='Escalated' and @role='option']")
            path_status = status.text
            driver.execute_script("arguments[0].click();", status)
            print("Click on Escalated button from Path")

            mark_button = driver.find_element(By.XPATH, "//span[@class='uiOutputText']")
            driver.execute_script("arguments[0].click();", mark_button)

            print("Click on Mark as Current Status button")

            case_status = driver.find_element(By.XPATH, "//lightning-formatted-text[@slot='output'][normalize-space()='Escalated']").text
            print("Updated Case Status is :"+ case_status)
            try:

                if path_status == case_status:
                    print("Assertion Passed")
                else:
                    print("Assertion Failed")
            except NoSuchElementException:
                pytest.fail("Status value not found")

            assert path_status == case_status, f"Assertion Failed: Expected '{path_status}' but got '{case_status}'"

        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")