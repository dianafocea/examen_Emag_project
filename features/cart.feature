Feature: Emag Cart Feature

    Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "Sterilised Nutrisavour"
      When products: I add product to basket "Hrana umeda pentru pisici Pro Plan Sterilised Nutrisavour, Pui in Sos, 10x85g"
      When products: I click Vezi detalii cos

    @cart_price
    Scenario: Test cart total price functionality
      Then cart: I verify that total price is correct "54,99"


    @cart_remove
    Scenario: Test cart remove product functionality
      When cart: I click sterge link
      Then cart: I verify empty cart message is displayed




