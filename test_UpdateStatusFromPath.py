import time
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser")
class TestUpdateStatusFromPath:

    def test_update_status_from_path(self, browser):
        driver = browser
        driver.implicitly_wait(20)

        try:
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Case/list?filterName=__Recent")
            print("\nGo to the Cases tab")

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
            print("Entered age as : 40")

            driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Click On Save")
            print("Case is Created")

            wait = WebDriverWait(driver, 10)
            case_number_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Case Number']/ancestor::div[contains(@class,'slds-form-element')]//lightning-formatted-text")))
            case_number = case_number_element.text

            print(f"The Case Number is: " + str(case_number))

            status = driver.find_element(By.XPATH, "//a[@title='Escalated' and @role='option']")
            path_status = status.text
            driver.execute_script("arguments[0].click();", status)
            print("Click on Escalated button from Path")

            mark_button = driver.find_element(By.XPATH, "//span[@class='uiOutputText']")
            driver.execute_script("arguments[0].click();", mark_button)
            print("Click on Mark as Current Status button")

            #wait = WebDriverWait(driver, 10)
            case_status_element = wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//lightning-formatted-text[@data-output-element-id='output-field'][normalize-space()='Escalated']")
                )
            )
            case_status = case_status_element.text
            print("Updated Case Status is: " + case_status)

            if path_status == case_status:
                print("Assertion Passed")
            else:
                print("Assertion Failed")

            assert path_status == case_status, f"Assertion Failed: Expected '{path_status}' but got '{case_status}'"

        except TimeoutException:
            pytest.fail("Element did not appear in time — possibly UI delay or wrong XPath.")
        except NoSuchElementException as e:
            pytest.fail(f"Element not found: {e}")
        except Exception as e:
            print(f"Unexpected error occurred:\n{e}")
            pytest.fail("Test failed due to unexpected exception.")
        finally:
            print("Exit from the class")
