import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
class TestCreateAsset:

    def test_create_asset(self,browser):
        driver = browser
        driver.implicitly_wait(20)

        try:
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Asset/list?filterName=AllAssets")
            print("\nGo to the Assets tab")

            driver.find_element(By.XPATH, "//div[@title='New']").click()
            print("Click on New button")

            driver.find_element(By.XPATH, "//input[@name='Name']").send_keys("New Asset from Automation")
            print("Entered Name as: New Asset from Automation")

            driver.find_element(By.XPATH, "//input[@name='SerialNumber']").send_keys("1234566666667")
            print("Entered Serial Number as: 1234566666667")

            driver.find_element(By.XPATH, "//input[@name='InstallDate']").send_keys("25/05/2025")
            print("Selected Install Date as : 25/05/2025")

            driver.find_element(By.XPATH, "//button[@aria-label='Status']").click()
            print("Click on Status")

            driver.find_element(By.XPATH, "//div[@aria-label='Status']// span[@title='Shipped']").click()
            print("Select Shipped")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Products...']").send_keys("SLA")
            print("Search for Product")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='01t5j00000BWmcZAAT']").click()
            print("Product selected as: SLA: Platinum")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Accounts...']").send_keys("G")
            print("Search for Account")
            driver.find_element(By.XPATH, "//div[@role='listbox']// lightning-base-combobox-item[@data-value='001J400000WkQHnIAN']").click()
            print("Account Selected")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Contacts...']").send_keys("New")
            print("Search for Contact")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='003J400000KMw5gIAD']").click()
            print("Contact Selected")

            driver.find_element(By.XPATH, "//input[@name='Quantity']").send_keys("12")
            print("Entered Quantity as: 12")

            driver.find_element(By.XPATH, "//input[@name='Price']").send_keys("100")
            print("Entered Price as: 100")

            driver.find_element(By.XPATH, "//textarea[@part='textarea']").send_keys("This Asset is creating from Selenium Automation")
            print("Entered Description as : This Asset is creating from Selenium Automation")

            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            print("Click On Save")
            print("Asset is Created")

        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")