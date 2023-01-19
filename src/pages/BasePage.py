from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from src.utils import config_reader
from src.utils.custom_logger import info_log, error_log


# Re-usable functions for page actions
# Logs the details of each web element into log file, console & allure report post the action

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Function to click web element
    def do_click(self, by_locator, description):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).click()
        info_log("Clicked on web element: " + description + "successfully")

    # Function to clear web element
    def do_clear(self, by_locator, description):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).clear()
        info_log("Cleared the content from web element: " + description + "successfully")

    # Function to set the text in web element
    def do_setText(self, by_locator, text, description):
        # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)
        info_log("Entered the text: " + text + " in web element: " + description + " successfully")

    # Function to get multiple web elements associated text:
    def get_elements_text(self, by_locator, description):
        elements = WebDriverWait(self.driver, 20).until(ec.visibility_of_all_elements_located(by_locator))
        text_list = []
        for ele in elements:
            un_trim_text = ele.text
            text_list.append(un_trim_text.strip())
        # print(f"text_list: {text_list}")
        info_log("Fetched text list from web element: " + description + "successfully")
        return text_list

    # Function to get single web element associated text:
    def get_element_text(self, by_locator, description):
        try:
            element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator))
            info_log("Fetched text list from web element: " + description + "successfully")
            return element.text
        except TimeoutException as err:
            print("Exception ignored")
        except NoSuchElementException as err:
            error_log(f"Web element: {description} text fetch failed due to: {err}")
            raise err

    # Function to get attribute value from the web element
    def get_attribute_value(self, by_locator, attribute, description):
        try:
            element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator))
            info_log("Fetched the attribute value: " + getattr(element,
                                                               attribute) + "from web element" + description + "successfully")
            return getattr(element, attribute)
        except TimeoutException as err:
            print("Exception ignored")
        except NoSuchElementException as err:
            error_log(f"Web element: {description} attribute fetch failed due to: {err}")
            raise err

    # Function to verify whether web element is visible
    def is_visible(self, by_locator, description):
        element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator))
        info_log("The web element: " + description + "is visible")
        return bool(element)

    # Function to get title of web page
    def get_title_value(self, exp_title):
        WebDriverWait(self.driver, 20).until(ec.title_is(exp_title))
        info_log("Fetched the title successfully: " + self.driver.title)
        return self.driver.title

    # Function to select the value from the drop down
    def select_value(self, by_locator, value, description):
        elements = WebDriverWait(self.driver, 20).until(ec.visibility_of_all_elements_located(by_locator))
        for ele in elements:
            un_trim_text = ele.text
            if value == un_trim_text.strip():
                ele.click()
                info_log(f"Selected: {value} successfully from {description} dropdown")

    # Function to wait for web element for a max of 25 sec
    def wait_for_element(self, by_locator, description):
        try:
            element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator))
            # info_log("Fetched text list from web element: " + description + "successfully")
            return bool(element)
        except UnboundLocalError as err:
            print("Exception ignored")
        except StaleElementReferenceException as err:
            print("Exception ignored")
        except NoSuchElementException as err:
            error_log(f"Web element: {description} load is taking longer tha usual: {err}")
            raise err

    # Function to wait for web element for a max of 25 sec
    def wait_for_elements(self, by_locator, description):
        try:
            elements = WebDriverWait(self.driver, 25).until(ec.visibility_of_all_elements_located(by_locator))
            # info_log("Fetched text list from web element: " + description + "successfully")
            return bool(elements)
        except UnboundLocalError as err:
            print("Exception ignored")
        except StaleElementReferenceException as err:
            print("Exception ignored")
        except NoSuchElementException as err:
            error_log(f"Web element: {description} load is taking longer tha usual: {err}")
            raise err

    # Function to wait for page title for a max of 25 sec
    def wait_for_title(self, exp_title):
        WebDriverWait(self.driver, 25).until(ec.title_is(exp_title))

    # Function to navigate to specific url
    def navigate(self, url, description):
        self.driver.get(config_reader.read_config("Env Info", url))
        info_log(f"Invoked: {description} successfully")

    # Function to scroll up
    def scroll_up(self):
        self.driver.find_element(By.XPATH,'//body').send_keys(Keys.CONTROL + Keys.HOME)

    # Function to scroll down
    def scroll_down(self):
        self.driver.find_element(By.XPATH,'//body').send_keys(Keys.CONTROL + Keys.END)

    # Function to click ENTER key
    def enter_key(self):
        self.driver.find_element(By.XPATH,'//body').send_keys(Keys.RETURN)
        info_log(f"Pressed key: ENTER successfully")

    # Function to click ENTER key
    def enterKey(self,by_locator):
        self.driver.find_element(by_locator).send_keys(Keys.RETURN)
        info_log(f"Pressed key: ENTER successfully")
