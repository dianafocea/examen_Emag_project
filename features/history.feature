Feature: Emag history feature

  Background:
    Given home: I am a user on emag.ro Home page

  @history_orders
  Scenario: Click comenzile mele to view my orders
    When home: I click on contul meu
    When login: I set my email "test_emag_itf@yopmail.com" and click Continua
    When login: I set my password "Test1234@" and click Continua
    When home: I click on contul meu
    When my_account: I click on vezi istoricul de comenzi
    Then history: I can see history page