import json

from behave import *
from selenium.webdriver import Keys
from src.pages.LoginPage import LoginPage
from src.utils import config_reader
from src.utils.custom_logger import info_log, error_log


@given(u'Navigate to Google Search Page')
def step_impl(context):
    try:
        context.loginPage = LoginPage(context.driver)
        context.loginPage.navigate("testurl", "Google")
        actual_title = context.loginPage.get_title_value(context.data.get("title_1"))
        assert actual_title == context.data.get("title_1")
        info_log(f"PASSED: Google Search Page launched successfully")
    except Exception as err:
        error_log(f"Google Search Page launch failed due to: {err}")
        raise err


@when(u'User enter the phrase as Selenium and click on Go')
def step_impl(context):
    try:
        context.loginPage.do_setText(context.loginPage.editbox_css, context.data.get("phrase"), "Searchbox")
        context.loginPage.do_click(context.loginPage.editbox_css, "Search box")
        context.loginPage.do_setText(context.loginPage.editbox_css, Keys.TAB, "Search box")
        context.loginPage.wait_for_element(context.loginPage.button_xpath, "Search button")
        context.loginPage.do_click(context.loginPage.button_xpath, "Search button")
        info_log(f"PASSED: Entered value and clicked on Go successfully")
    except Exception as err:
        error_log(f"Setting the text and click on Go failed due to: {err}")
        raise err


@then(u'Verify the title of the web page')
def step_impl(context):
    try:
        context.loginPage.wait_for_title(context.data.get("title_2"))
        actual_title = context.loginPage.get_title_value(context.data.get("title_2"))
        # Code to write the date into json file
        file_name = '.\\test_data\\data.json'
        context.data["output_data"] = actual_title
        output_stream = open(file_name,"w")
        json.dump(context.json_array,output_stream)

        assert actual_title == context.data.get("title_2")
        info_log(f"PASSED: Google page title: {actual_title} validated successfully")
    except Exception as err:
        error_log(f"Title verification failed due to: {err}")
        raise err
