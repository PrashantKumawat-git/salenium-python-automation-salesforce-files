import time
import pytest
from selenium.webdriver.common.by import By
from Utility.utilities import Utilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read data from an Excel file
lead_data = Utilities.read_data_from_excel(r"C:\Selenium-Python\PythonSeleniumProject\SalesforceProjects\testdata\leads.xlsx", "Sheet1")

@pytest.mark.usefixtures("browser")
class TestCreateLeadViaExcel:
    @pytest.mark.parametrize("FirstName, LastName, Company, Title, Phone, Email, Website, LeadSource, Rating", lead_data)
    def test_create_lead_via_excel(self, browser, FirstName, LastName, Company, Title, Phone, Email, Website, LeadSource, Rating):

        try:
            driver = browser
            wait = WebDriverWait(driver, 15)
            driver.implicitly_wait(10)

            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Lead/list?filterName=__Recent")
            print("\nNavigated to the Leads tab")

            driver.find_element(By.XPATH, "//div[@title='New']").click()
            print("Clicked on New button")

            driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys(FirstName)
            print(f"Entered First Name as :" + FirstName)

            driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys(LastName)
            print(f"Entered Last Name as :" + LastName)

            driver.find_element(By.XPATH, "//input[@name='Company']").send_keys(Company)
            print(f"Entered Company as :" + Company)

            driver.find_element(By.XPATH, "//input[@name='Title']").send_keys(Title)
            print(f"Entered Title as :" + Title)

            driver.find_element(By.XPATH, "//input[@name='Phone']").send_keys(Phone)
            print(f"Entered Phone as :" + str(Phone))

            driver.find_element(By.XPATH, "//input[@name='Email']").send_keys(Email)
            print(f"Entered Email as :" + Email)

            driver.find_element(By.XPATH, "//input[@name='Website']").send_keys(Website)
            print(f"Entered Website as :" + Website)

            driver.find_element(By.XPATH, "//button[@aria-label='Lead Source']").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@title='{LeadSource}']"))).click()
            print("Selected Lead Source as Web")

            driver.find_element(By.XPATH, "//button[@aria-label='Rating']").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@title='{Rating}']"))).click()
            print("Selected Rating as Web")

            driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            print("Clicked on Save")
            print("Lead is Created")

        except Exception as e:
            print(e)