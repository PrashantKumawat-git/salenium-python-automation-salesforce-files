import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
class TestCreateWorkOrder:

    def test_create_work_order(self,browser):
        driver = browser
        driver.implicitly_wait(20)

        try:
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Entitlement/list?filterName=All_Entitlements")
            print("\nGo to the Entitlements tab")

            driver.find_element(By.XPATH, "//div[@class='oneConsoleObjectHome']//div[@title='New'][normalize-space()='New']").click()
            print("Click on New button")

            driver.find_element(By.XPATH, "//input[@name='Name']").send_keys("New Entitlement from Automation")
            print("Entered Name as: New Entitlement from Automation")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Accounts...']").send_keys("G")
            print("Search for Account")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='001J400000WkQHnIAN']").click()
            print("Account Selected")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Assets...']").send_keys("Zend")
            print("Search for Asset")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='02iJ4000000zIGfIAM']").click()
            print("Asset selected")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Service Contracts...']").send_keys("Man")
            print("Search Service Contracts...")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='810J4000000CegqIAC']").click()
            print("Service Contracts selected")

            driver.find_element(By.XPATH, "//input[@name='StartDate']").send_keys("25/05/2025")
            print("Selected Start Date as : 25/05/2025")

            driver.find_element(By.XPATH, "//input[@name='EndDate']").send_keys("25/05/2035")
            print("Selected End Date as : 25/05/2035")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Business Hours...']").send_keys("Def")
            print("Search Business Hours...")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='01m5j000001JypiAAC']").click()
            print("Business Hours selected as : Default")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Entitlement Processes...']").send_keys("Stand")
            print("Search Entitlement Processes...")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='5525j0000092y1sAAA']").click()
            print("Entitlement Processes as : Standard Case")

            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            print("Click On Save")
            print("Entitlement is Created")

        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")