Feature: Verify Page title

  Scenario: TC01 - Validating page title
    Given Navigate to Google Search Page
    When User enter the phrase as Selenium and click on Go
    Then Verify the title of the web page
