# ----------------------------------------------------------------------------
# File: OrderPage.feature
# Autor: Kosalram
# Date: 3-8-2016
# ----------------------------------------------------------------------------

Feature:  Order an iteam from the e-commerce website.

   @order_page
  Scenario: Order an iteam and verify the result
    Given Goto home page
    When I search for RETRO item
    Then I should get RETRO CHIC EYEGLASSES
    When I order the product
    Then Then I should get it in my shopping cart