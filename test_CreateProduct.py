import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser")
class TestCreateProduct:

    def test_create_product(self,browser):
        driver = browser
        driver.implicitly_wait(20)

        try:
            wait = WebDriverWait(driver, 10)
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Product2/list?filterName=AllProducts")
            print("\nGo to the Product tab")

            driver.find_element(By.XPATH, "//div[@title='New']").click()
            print("Click on New button")

            driver.find_element(By.XPATH, "//input[@name='Name']").send_keys("SLA : Titanium")
            print("Entered Product Name as: SLA : Titanium")

            driver.find_element(By.XPATH, "//input[@name='ProductCode']").send_keys("SLA9010")
            print("Entered Product Code as: SLA9010")

            driver.find_element(By.XPATH, "//input[@name='IsActive']").send_keys("SLA9010")
            print("Click on Active checkbox")

            driver.find_element(By.XPATH, "//button[@aria-label='Product Family']").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@title='Retail']"))).click()
            print("Selected Product Family as Retail")

            driver.find_element(By.XPATH, "//button[@aria-label='Shipment Status']").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@title='Order Accepted']"))).click()
            print("Selected Shipment Status as Order Accepted")

            driver.find_element(By.XPATH, "//textarea[@part='textarea']").send_keys(
                "This Product is creating from Selenium Automation")
            print("Entered Description as : This Product is creating from Selenium Automation")

            driver.find_element(By.XPATH, "//input[@name='Expected_delivery_date__c']").send_keys("25/05/2035")
            print("Selected Expected_delivery_date__c as : 25/05/2035")

            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            print("Click On Save")
            print("Product is Created")
            print("Product Name is: SLA : Titanium")

        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")