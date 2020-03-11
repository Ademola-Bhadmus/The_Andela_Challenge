from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from behave import *
from Features.helper import values

driver = webdriver.Chrome()

use_step_matcher("re")


@given("I am on the login page for the myandela app")
def step_impl(context):
    driver.maximize_window()
    driver.get(values.url)


@when("I insert my login with valid details")
def step_impl(context):
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,values.usrFld)))
    driver.find_element_by_id(values.usrFld).send_keys(values.email)
    driver.find_element_by_name(values.pwdFld).send_keys(values.pasword)


@step("I click the Sign In button")
def step_impl(context):
    driver.find_element_by_id(values.signBtn).click()


@step("I click on add new skill")
def step_impl(context):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, values.newskill)))
    driver.find_element_by_css_selector(values.newskill).click()


@step("I fill in the details")
def step_impl(context):
    driver.find_element_by_name(values.skNameFld).send_keys(values.skName)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, values.sklOpt))).click()
    driver.find_element_by_css_selector(values.drpDown).click()
    driver.find_element_by_css_selector(values.proLvl).click()
    driver.find_element_by_name(values.exper).send_keys(values.years)
    content = driver.find_element_by_css_selector(values.skill_content)

    try:
        assert values.warning in content.text
        print("Assertion Passed!")

    except Exception as e:
        print("Assertion Failed")



@step("I click the Add Skill button")
def step_impl(context):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, values.addSkillBtn))).click()


@then("It should add successfully")
def step_impl(context):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, values.skillBadge)))
    badge = driver.find_element_by_css_selector(values.skillBadge)

    try:
        assert values.skName in badge.text
        print("Assertion Passed!!")

    except Exception as e:
        print("Assertion Failed")

    driver.quit()


