import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function", autouse=True)
def browser():
    try:
        edge_options = Options()
        edge_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1  # 1 = Allow, 2 = Block
        })
        driver = webdriver.Edge(options=edge_options)
        print("Open Edge browser")
        driver.maximize_window()
        print("Maximize the window")
        driver.implicitly_wait(20)

        # Login to Salesforce
        driver.get("https://login.salesforce.com/")
        print("Go to the login Url")
        driver.find_element(By.ID, "username").send_keys("Your username")
        print("Entered Username")
        driver.find_element(By.ID, "password").send_keys("your password")
        print("Entered Password")
        driver.find_element(By.ID, "Login").click()
        print("Logged into Salesforce")

        # Wait for the home page to load (App Launcher should be available)
        app_launcher = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='slds-icon-waffle']"))
        )
        print("Home page loaded successfully")
        app_launcher.click()
        print("Clicked on App Launcher")
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//input[contains(@placeholder,'Search apps') or contains(@placeholder,'Search apps and items')]"))
        )
        search_field.clear()

        # Search for Sales App
        search_field.send_keys("Sales")
        print("Searching for Sales...")
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='07p5j0000003V8hAAE']//b[contains(text(),'Sales')]").click()
        print("Click on Sales App")
        time.sleep(2)
        yield driver

        driver.quit()
        print("Quit the browser")

    except Exception as e:
        print(e)

#create the HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    driver = item.funcargs.get("browser", None)

    def is_driver_alive(driver):
        try:
            # A harmless command to check if session is alive
            driver.title
            return True
        except Exception:
            return False

    if report.when in ("setup", "call", "teardown") and driver and is_driver_alive(driver):
        htmlpath = getattr(item.config.option, "htmlpath", None)
        if htmlpath:
            report_directory = os.path.dirname(htmlpath)
        else:
            report_directory = "reports"
        screenshots_dir = os.path.join(report_directory, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        file_name = f"{report.nodeid.replace('::', '_')}_{report.when}_{report.outcome}.png"
        file_name = file_name.replace("/", "_").replace("\\", "_")
        destination_file = os.path.join(screenshots_dir, file_name)

        # Extract method name only from nodeid (which looks like 'test_module.py::TestClass::test_method')
        #method_name = report.nodeid.split("::")[-1]
        # Format: ddmm_HHMMSS
        #timestamp = datetime.datetime.now().strftime('%d%m_%H%M%S')
        # Final compact unique filename
        #file_name = f"{method_name}_{timestamp}.png"
        # Safe full path
        #destination_file = os.path.join(screenshots_dir, file_name)

        # Screenshot
        try:
            driver.save_screenshot(destination_file)
            html = (
                f'<div><img src="screenshots/{file_name}" alt="screenshot" '
                'style="width:300px;height:200px;" '
                'onclick="window.open(this.src)" align="right"/></div>'
            )
            extra.append(pytest_html.extras.html(html))
        except Exception as e:
            print("Screenshot error:", e)

        # Current URL
        try:
            current_url = driver.current_url
            extra.append(pytest_html.extras.url(current_url))
        except Exception as e:
            print("URL capture error:", e)

    report.extra = extra


def pytest_html_report_title(report):
    report.title = "Pytest HTML Report with Screenshots and Link"
