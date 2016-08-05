# ----------------------------------------------------------------------------
# File: MainPages.py
# Autor: Kosalram
# Date: 2-8-2016
# ----------------------------------------------------------------------------

from behave import given, when, then
from hamcrest import assert_that, equal_to


@given('"{page_link}"')
def step_impl(context,page_link):
    context.page_link = page_link


@when('opeaning page link')
def step_impl(context):
    context.browser.get(context.page_link)

@then('must have "{page_title}"')
def step_impl(context,page_title):
    context.page_title = page_title
    assert_that(context.browser.title, equal_to(context.page_title))