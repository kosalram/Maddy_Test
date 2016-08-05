# ----------------------------------------------------------------------------
# File: MainPages.feature
# Autor: Kosalram
# Date: 2-8-2016
# ----------------------------------------------------------------------------

Feature:  Make sure all the main pages are working properly.

@main_pages
Scenario Outline: Main Pages
    Given "<page link>"
    When opeaning page link
    Then must have "<page title>"

Examples: Main Pages
    | page link | page title |
    | http://magento-demo.lexiconn.com/  | Madison Island |
    | http://magento-demo.lexiconn.com/vip.html | VIP     |
    | http://magento-demo.lexiconn.com/sale.html | Sale   |
    | http://magento-demo.lexiconn.com/catalog/seo_sitemap/category/ |Site Map|
    | http://magento-demo.lexiconn.com/about-magento-demo-store/     |About Us|
    | http://magento-demo.lexiconn.com/sales/guest/form/             |Magento Commerce|
    | http://magento-demo.lexiconn.com/privacy-policy-cookie-restriction-mode/ |Privacy Policy|
    | http://magento-demo.lexiconn.com/customer/account/create/                |Create New Customer Account|
    | http://magento-demo.lexiconn.com/customer/account/login/                 |Customer Login|

