import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import json
import allure
from selenium import webdriver
from src.utils import config_reader


def before_scenario(context, scenario):
    if config_reader.read_config("Env Info","browser") == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("excludeSwitches",["enable-logging"])
        # options.add_argument('--headless')
        # options.add_argument("--windo-size=1500,1000")
        context.driver = webdriver.Chrome(options=options,executable_path=".\\drivers\\chromedriver.exe")
    elif config_reader.read_config("Env Info","browser") == "firefox":
        context.driver = webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
    elif config_reader.read_config("Env Info","browser") == "edge":
        context.driver = webdriver.Edge(executable_path="./drivers/msedgedriver.exe")
    context.driver.maximize_window()
    context.driver.delete_all_cookies()
    sc_name = context.scenario.name
    tid = sc_name.split("-")
    context.testid = tid[0].strip()
    input_file = open('./test_data/data.json')
    context.json_array = json.load(input_file)
    context.data = context.json_array.get(context.testid)
    print(f"context.testid: {context.testid}")
    print(f"Executing Scenario name: {context.scenario.name}")


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
