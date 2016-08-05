# ----------------------------------------------------------------------------
# File: SearchPages.py
# Autor: Kosalram
# Date: 3-8-2016
# ----------------------------------------------------------------------------

from behave import given, when, then
from hamcrest import assert_that, equal_to

@given('I am on the home page')
def step_impl(context):
    context.browser.get(context.url)

@then('Then I should see page title Madison Island')
def step_impl(context):
    title_vlaue="Madison Island"
    assert_that(context.browser.title, equal_to(title_vlaue))

@when('I search for RETRO')
def step_impl(context):
    search = context.browser.find_element_by_id("search")
    search.send_keys("RETRO")
    search.submit()


@then('I should get RETRO CHIC EYEGLASSES in search result page')
def step_impl(context):
    prod_name = context.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a").text
   #goolge chrome xpath value "//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a" not working
    assert "RETRO CHIC EYEGLASSES" in prod_name