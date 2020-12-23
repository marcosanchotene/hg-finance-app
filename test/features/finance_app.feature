Feature: HostGator finance application login page
  As a HostGator user,
  I want to load the finance application login page
  So I can perform login and related operations.

  Scenario: Blank email and blank password
    Given I am a registered user
    And I go to the login page
    When I click on the Entendi button
    And I type a "blank" email address
    And I type a "blank" password
    And I click on the Entrar button
    Then the email should be considered invalid

  Scenario: Valid password but email address does not have @ symbol
    Given I am a registered user
    And I go to the login page
    When I click on the Entendi button
    And I type an email address "without the @ symbol"
    And I type a "valid" password
    And I click on the Entrar button
    Then the email should be considered invalid

  Scenario: Valid password but email address is blank after @ symbol
    Given I am a registered user
    And I go to the login page
    When I click on the Entendi button
    And I type an email address "blank after the @ symbol"
    And I type a "valid" password
    And I click on the Entrar button
    Then the email should be considered invalid

  Scenario: Valid email but password is not typed
    Given I am a registered user
    And I go to the login page
    When I click on the Entendi button
    And I type a "valid" email address
    And I type a "blank" password
    And I click on the Entrar button
    Then the password should be considered invalid

  Scenario: Valid email but password is invalid
    Given I am a registered user
    And I go to the login page
    When I click on the Entendi button
    And I type a "valid" email address
    And I type an "invalid" password
    And I click on the Entrar button
    Then the password should be considered invalid

  Scenario: Valid email and password but recaptcha image is not clicked on
    Given I am a registered user
    And I go to the login page
    When I click on the Entendi button
    And I type a "valid" email address
    And I type a "valid" password
    And I click on the Entrar button
    Then the recaptcha message should be displayed

  Scenario: Clicking on 'Esqueceu sua senha?' link
    Given I am a registered user
    And I go to the login page
    When I click on the Entendi button
    And I click on the Esqueceu sua senha? link
    Then the password reset page should be loaded

  Scenario: Clicking on 'base de conhecimento' link
    Given I am a registered user
    And I go to the login page
    When I click on the Entendi button
    And I click on the base de conhecimento link
    Then the support page should be loaded on a new tab
