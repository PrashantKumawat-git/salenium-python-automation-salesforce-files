import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("browser")
class TestCreateWorkOrder:

    def test_create_work_order(self,browser):
        driver = browser
        driver.implicitly_wait(20)

        try:
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/WorkOrder/list?filterName=All_WorkOrders")
            print("\nGo to the Work Order tab")

            driver.find_element(By.XPATH, "(//div[@title='New'][normalize-space()='New'])[1]").click()
            print("Click on New button")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Cases...']").send_keys("Rep")
            print("Search for Case")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='500J400000HUxMaIAL']").click()
            print("Case selected")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Contacts...']").send_keys("New")
            print("Search for Contacts")
            driver.find_element(By.XPATH, "//div[@role='listbox']// lightning-base-combobox-item[@data-value='003J400000KMw5gIAD']").click()
            print("Contact selected")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Accounts...']").send_keys("G")
            print("Search for Account")
            driver.find_element(By.XPATH, "//div[@role='listbox']// lightning-base-combobox-item[@data-value='001J400000WkQHnIAN']").click()
            print("Account Selected")

            driver.find_element(By.XPATH, "//input[@name='Subject']").send_keys("New Work Order From Automation")
            print("Entered Subject as : New Work Order From Automation")

            driver.find_element(By.XPATH, "//textarea[@part='textarea']").send_keys("This Work Order is creating from Selenium Automation")
            print("Entered Description as : This Work Order is creating from Selenium Automation")

            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            print("Click On Save")
            print("Work Order is Created")

            wait = WebDriverWait(driver, 10)
            wo_number_element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                               "//span[text()='Work Order Number']/ancestor::div[contains(@class,'slds-form-element')]//lightning-formatted-text")))
            wo_number = wo_number_element.text
            print(f"The Work Order Number is: " + str(wo_number))

            driver.find_element(By.XPATH, "//a[@data-label='Related']").click()
            print("Click on New Related")

            driver.find_element(By.XPATH, "//li[@data-target-selection-name='sfdc:StandardButton.WorkOrderLineItem.New']//a[@title='New']").click()
            print("Click on New button")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Orders...']").send_keys("00000")
            print("Search for Order")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='801J4000005UuAVIA0']").click()
            print("Order selected")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Assets...']").send_keys("Zend")
            print("Search for Asset")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='02iJ4000000zIGfIAM']").click()
            print("Asset selected")

            driver.find_element(By.XPATH, "//textarea[@part='textarea']").send_keys(
                "This Work Order Line Item is creating from Selenium Automation")
            print("Entered Description as : This Work Order Line Item is creating from Selenium Automation")

            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            print("Click on Save Button")

            woli_number_element = wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr[1]/th[1]/lightning-primitive-cell-factory[1]/span[1]/div[1]")))
            wo_li_number = woli_number_element.text
            for word in wo_li_number.split():
                if word.isdigit():
                    woli_number = word
                    break

            print(f"The Work Order Line Item Number is: " + woli_number)


        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")