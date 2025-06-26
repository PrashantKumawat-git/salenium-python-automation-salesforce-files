
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("browser")
class TestVerifyCaseOnContact:

    def test_verify_case_on_contact(self,browser):
        driver = browser
        driver.implicitly_wait(10)

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
            print("Selected Resolution Date as : New Case for Testing")
            driver.find_element(By.XPATH, "//input[@name='Age__c']").send_keys("18")
            print("Entered age as : 18")
            driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Click On Save")
            print("Case is Created")

            wait = WebDriverWait(driver, 10)
            case_number_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Case Number']/ancestor::div[contains(@class,'slds-form-element')]//lightning-formatted-text")))
            case_number = case_number_element.text

            print(f"The Case Number is: " + str(case_number))

            driver.find_element(By.XPATH, "//a//span[contains(text(),'New Test Contact')]").click()
            print("Click on the Contact")

            caseoncontact = driver.find_element(By.XPATH, f"//span[@class='slds-truncate']//span[contains(text(),'{case_number}')]").text
            print("The Case Number is: " + str(caseoncontact))

            assert case_number == caseoncontact
            print("Assertion Passed: Case number is linked in Contact's Cases related list")

        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")