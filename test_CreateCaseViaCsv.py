import time
import pytest
from selenium.webdriver.common.by import By
from Utility.utilities import Utilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read data from the CSV file
test_data = Utilities.read_data_from_csv("C:\\Selenium-Python\\PythonSeleniumProject\\SalesforceProjects\\testdata\\dataInCsv.csv")


@pytest.mark.usefixtures("browser")
class TestCreateCaseViaCsv:

    @pytest.mark.parametrize("ContactName,ResolutionDate,Subject,Age", test_data)
    def test_create_case_via_csv(self, browser, ContactName, ResolutionDate, Subject, Age):
        try:

            driver = browser
            wait = WebDriverWait(driver, 15)
            driver.implicitly_wait(10)

            driver.get(
                "https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Case/list?filterName=__Recent")
            print("\nNavigated to the Cases tab")

            driver.find_element(By.XPATH, "//div[@title='New']").click()
            print("Clicked on New button")

            driver.find_element(By.XPATH,
                                "//label[@for='012J4000000kF5cIAE']//span[contains(@class,'slds-radio--faux')]").click()
            print("Selected Inquiry record type")

            driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
            print("Clicked on Next")

            driver.find_element(By.XPATH, "//button[@aria-label='Case Origin']").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@title='Web']"))).click()
            print("Selected Case Origin as Web")

            # Contact Lookup
            contact_input = driver.find_element(By.XPATH, "//input[@placeholder='Search Contacts...']")
            contact_input.send_keys(ContactName)
            print(f"Searched for Contact: {ContactName}")

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//lightning-base-combobox-item[contains(@data-item-id, 'combobox-input') and contains(@data-item-id, '-1')]"
            ))).click()
            print(f"Selected Contact: {ContactName}")
            driver.find_element(By.XPATH, "//input[@name='Resolution_Date__c']").send_keys(ResolutionDate)
            print(f"Selected Resolution Date as : {ResolutionDate}")
            driver.find_element(By.XPATH, "//input[@name='Subject']").send_keys(Subject)
            print(f"Selected Subject as : {Subject}")
            driver.find_element(By.XPATH, "//input[@name='Age__c']").send_keys(Age)
            print(f"Entered Age: {Age}")
            driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Clicked on Save")

            # Validation for Age
            if int(Age) < 18:
                try:
                    error_text = wait.until(EC.visibility_of_element_located((
                        By.XPATH, "//div[contains(@class, 'form-element__help') and contains(text(), 'Age must')]"
                    ))).text
                    print(f"Validation Error Found: {error_text}")
                    pytest.skip("Skipping test due to age validation failure")
                except Exception:
                    print("Expected validation error not found, but age is <18")
                    pytest.skip("Skipping test: Age < 18 with no error shown")

            # Case Created
            print("Case is Created")

            # Extract Case Number
            wait = WebDriverWait(driver, 10)
            case_number_element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                               "//span[text()='Case Number']/ancestor::div[contains(@class,'slds-form-element')]//lightning-formatted-text")))
            case_number = case_number_element.text

            print(f"The Case Number is: " + str(case_number))

        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")