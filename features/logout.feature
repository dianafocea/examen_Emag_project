Feature: Emag logout feature

    Background:
      Given home: I am a user on emag.ro Home page

    @logout
    Scenario: Test that a logged in user is successfuly loged out
      When home: I click on contul meu
      When login: I set my email "test_emag_itf@yopmail.com" and click Continua
      When login: I set my password "Test1234@" and click Continua
      When home: I hover over contul meu
      When home: I click logout button
      Then home: I verify home page url


