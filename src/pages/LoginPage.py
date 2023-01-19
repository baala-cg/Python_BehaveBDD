from selenium.webdriver.common.by import By

from src.pages.BasePage import BasePage

# Inherit the BasePage functions in this page file

class LoginPage(BasePage):

    # Element locators for LoginPage
    editbox_css = By.CSS_SELECTOR, "[name='q']"
    button_xpath = By.XPATH, "(//input[@name='btnK'])[2]"



    # Page specific methods for LoginPage

    def __init__(self, driver):
        super().__init__(driver)

