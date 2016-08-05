# ----------------------------------------------------------------------------
# File: ProductPage.feature
# Autor: Kosalram
# Date: 3-8-2016
# ----------------------------------------------------------------------------

Feature:  Open the product details page and verify the product.

  @product_page
  Scenario: Product Details Page Verification
    Given Load home page
    When I search RETRO
    Then I should get RETRO CHIC EYEGLASSES in result page
    When I open the product
    Then Then I should get Retro Chic Eyeglasses in page title