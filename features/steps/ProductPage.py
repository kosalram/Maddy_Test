# ----------------------------------------------------------------------------
# File: ProductPage.py
# Autor: Kosalram
# Date: 3-8-2016
# ----------------------------------------------------------------------------

from behave import given, when, then
from hamcrest import assert_that, equal_to

@given('Load home page')
def step_impl(context):
    context.browser.get(context.url)

@when('I search RETRO')
def step_impl(context):
    search = context.browser.find_element_by_id("search")
    search.send_keys("RETRO")
    search.submit()


@then('I should get RETRO CHIC EYEGLASSES in result page')
def step_impl(context):
    context.prod_link = context.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a")
    product_name=context.prod_link.text
    #goolge chrome xpath value "//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a" not working
    assert "RETRO CHIC EYEGLASSES" in product_name

@when('I open the product')
def step_impl(context):
    context.prod_link.click()

@then('Then I should get Retro Chic Eyeglasses in page title')
def step_impl(context):
    assert_that(context.browser.title, equal_to("Retro Chic Eyeglasses"))

# How to execute common steps in different step files?.