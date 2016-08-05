# ----------------------------------------------------------------------------
# File: SearchPage.feature
# Autor: Kosalram
# Date: 2-8-2016
# ----------------------------------------------------------------------------

Feature:  Open the search result page and look for an item and verify the result.

  @search_page
  Scenario: Search Result Page Verification
    Given I am on the home page
    Then Then I should see page title Madison Island
    When I search for RETRO
    Then I should get RETRO CHIC EYEGLASSES in search result page