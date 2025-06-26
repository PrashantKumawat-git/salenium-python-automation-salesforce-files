import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser")
class TestCreateServiceAppointment:

    def test_create_service_appointment(self,browser):
        driver = browser
        driver.implicitly_wait(20)

        try:
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/ServiceAppointment/list?filterName=All_ServiceAppointments")
            print("\nGo to the Service Appointment tab")

            driver.find_element(By.XPATH, "//div[@title='New']").click()
            print("Click on New button")

            driver.find_element(By.XPATH, "//input[@placeholder='Search Contacts...']").send_keys("New")
            print("Search for Contacts...")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='003J400000KMw5gIAD']").click()
            print("Contact Selected")

            driver.find_element(By.XPATH, "//textarea[@part='textarea']").send_keys(
                "This Service Appointment is creating from Selenium Automation")
            print("Entered Description as : This Service Appointment is creating from Selenium Automation")

            driver.find_element(By.XPATH, "//input[@name='EarliestStartTime']").send_keys("25/05/2025")
            print("Selected Earliest Start Time as : 25/05/2025")

            driver.find_element(By.XPATH, "//input[@name='DueDate']").send_keys("25/05/2035")
            print("Selected Due Date as : 25/05/2035")

            driver.find_element(By.XPATH, "//input[@placeholder='Search...']").send_keys("G")
            print("Search Parent Account...")
            driver.find_element(By.XPATH,
                                "//div[@role='listbox']// lightning-base-combobox-item[@data-value='001J400000WkQHnIAN']").click()
            print("Parent Account selected")

            driver.find_element(By.XPATH, "//input[@name='Subject']").send_keys("New Service Appointment from Automation")
            print("Entered Subject as: New Service Appointment from Automation")

            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            print("Click On Save")
            print("Service Appointment is Created")

            wait = WebDriverWait(driver, 10)
            sa_number_element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//span[text()='Appointment Number']/ancestor::div[contains(@class,'slds-form-element')]//lightning-formatted-text")))
            sa_number = sa_number_element.text
            print(f"The Case Number is: " + str(sa_number))

        except Exception as e:
            print(e)
        finally:
            print("Exit from the class")