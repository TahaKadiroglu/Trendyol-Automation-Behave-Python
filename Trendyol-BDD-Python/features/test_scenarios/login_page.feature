Feature: Trendyol Automation Framework

  Scenario Outline: Success Login after Failure Login Tries
    Given Launch The Chrome Browser
    When Open TrendyolHomePage and Click Login Button
    Then Enter username "<username>" and password "<password>"
    Then Search for Iphone13 and Filter the products
    Then Open Product Page
    Then Go to Box Page



    Examples:
      | username | password |
      | tester123taha@gmail.com    | A789456. |





