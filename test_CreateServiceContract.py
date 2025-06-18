import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
class TestCreateServiceContracts:

    def test_create_service_contracts(self,browser):
        driver = browser
        driver.implicitly_wait(20)

        try:
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/ServiceContract/list?filterName=All_ServiceContracts")
            print("\nGo to the Service Contracts tab")

            driver.find_element(By.XPATH, "//div[@title='New']").click()
            print("Click on New button")

            driver.find_element(By.XPATH, "//input[@name='Name']").send_keys("New Service Contract from Automation")
            print("Entered Name as: New Service Contract from Automation")

            driver.find_element(By.XPATH, "//textarea[@part='textarea']").send_keys(
                "This Service Contract is creating from Selenium Automation")
            print("Entered Description as : This Service Contract is creating from Selenium Automation")

            driver.find_element(By.XPATH, "//input[@name='Term']").send_keys("12")
            print("Entered Term as: 12")

            driver.find_element(By.XPATH, "//input[@name='StartDate']").send_keys("25/05/2025")
            print("Selected Start Date as : 25/05/2025")

            driver.find_element(By.XPATH, "//input[@name='EndDate']").send_keys("25/05/2028")
            print("Selected End Date as : 25/05/2028")

            driver.find_element(By.XPATH, "//input[@name='ShippingHandling']").send_keys("10000")
            print("Selected Shipping Handling as : 10000")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Accounts...']").send_keys("G")
            print("Search for Account")
            driver.find_element(By.XPATH, "//div[@role='listbox']// lightning-base-combobox-item[@data-value='001J400000WkQHnIAN']").click()
            print("Account Selected")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Contacts...']").send_keys("New")
            print("Search for Contacts")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='003J400000KMw5gIAD']").click()
            print("Contact Selected")

            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            print("Click On Save")
            print("Service Contract is Created")

        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")