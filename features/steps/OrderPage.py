# ----------------------------------------------------------------------------
# File: OrderPage.py
# Autor: Kosalram
# Date: 3-8-2016
# ----------------------------------------------------------------------------

from behave import given, when, then
from hamcrest import assert_that, equal_to

@given('Goto home page')
def step_impl(context):
    context.browser.get(context.url)

@when('I search for RETRO item')
def step_impl(context):
    search = context.browser.find_element_by_id("search")
    search.send_keys("RETRO")
    search.submit()


@then('I should get RETRO CHIC EYEGLASSES')
def step_impl(context):
    prod_link = context.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a")
    product_name=prod_link.text
    #goolge chrome xpath value "//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a" not working
    assert "RETRO CHIC EYEGLASSES" in product_name

@when('I order the product')
def step_impl(context):
    add_to_cart = context.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/div[2]/button")
    add_to_cart.send_keys("\n") #We can use "\n" instead of ".click()"

@then('Then I should get it in my shopping cart')
def step_impl(context):
    success_msg = context.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[2]/ul/li/ul/li/span")
    assert_that(success_msg.text, equal_to("Retro Chic Eyeglasses was added to your shopping cart."))