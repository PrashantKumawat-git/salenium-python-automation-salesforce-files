import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
class TestVerifySumOfOppAmt:
    try:

        def test_sum_of_opportunities(self, browser):
            driver = browser
            driver.get("https://appsavio59-dev-ed.develop.lightning.force.com/lightning/o/Account/list?filterName=AllAccounts")
            print("\nGo to the Accounts page")
            driver.find_element(By.XPATH, "//li[@data-target-selection-name='sfdc:StandardButton.Account.New']//a[@title='New']").click()
            print("Click on the New button")

            # Fill Account details
            driver.find_element(By.XPATH, "//input[@name='Name']").send_keys("New Test 1001")
            driver.find_element(By.XPATH, "//input[@name='Phone']").send_keys("9876543210")
            driver.find_element(By.XPATH, "//input[@name='Site']").send_keys("Customer")
            print("Site is filled as : Customer")
            try:
                driver.find_element(By.XPATH, "//button[@aria-label='Rating']").click()
                driver.find_element(By.XPATH, "//div[@aria-label='Rating']//lightning-base-combobox-item[@data-value='Warm']").click()
            except Exception as e:
                print(f"Rating selection skipped: {e}")

            driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
            print("Account record is created")

            # Read initial sum of opportunity amount
            initial_oppoamnt = driver.find_element(By.XPATH, "//records-record-layout-item[@field-label='Sum of Opp. Amount']//lightning-formatted-text").text
            print("Initial SumOfOppoAmount is: " + initial_oppoamnt)

            self.create_related_oppo(driver, "Opp 101", 10000)
            current_oppoamnt = driver.find_element(By.XPATH,
                                                   "//records-record-layout-item[@field-label='Sum of Opp. Amount']//lightning-formatted-text").text

            print("After one opp the SumOfOppoAmount is: " + current_oppoamnt)
            self.create_related_oppo(driver, "Opp 102", 15000)


            # Final amount check
            final_oppoamnt = driver.find_element(By.XPATH, "//records-record-layout-item[@field-label='Sum of Opp. Amount']//lightning-formatted-text").text
            print("Final SumOfOppoAmount is: " + final_oppoamnt)

            cleaned_amount = final_oppoamnt.replace('₹', '').replace(',', '').split('.')[0]
            assert int(cleaned_amount) == 10000 + 15000
            print("Assertion Passed: Opportunities Amount is correct")

        def create_related_oppo(self, driver, name, amount):
            driver.find_element(By.XPATH, "//button[normalize-space()='New Opportunity']").click()
            print("Clicked on 'New Opportunity' button")

            driver.find_element(By.XPATH, "//input[@maxlength='120']").send_keys(name)
            print("Opportunity name filled as: " + name)

            driver.find_element(By.XPATH, "//a[@role='combobox']").click()
            driver.find_element(By.XPATH, "//a[@role='option' and @title='Value Proposition']").click()

            driver.find_element(By.XPATH, "//input[@step ='1']").send_keys(str(amount))
            print("Amount entered as: " + str(amount))

            driver.find_element(By.XPATH, "//button[contains(@class,'slds-button_brand') and .//span[text()='Save']]").click()
            print("Opportunity created")
            time.sleep(3)
    except Exception as e:
        print(e)

    finally:
        print("Exit from the class")