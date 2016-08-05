# -*- coding: UTF-8 -*-
# ----------------------------------------------------------------------------
# File: environment.py
# Autor: Kosalram
# Date: 2-8-2016
# ----------------------------------------------------------------------------

from selenium import webdriver

def before_all(context):

    context.browser = webdriver.Chrome()
    context.url="http://magento-demo.lexiconn.com/"

def after_all(context):

    context.browser.quit()
