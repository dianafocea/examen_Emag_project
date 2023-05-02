Feature: Emag Cart Feature

    Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "Samsung S21 FE 128 white"
      When home: I click Tip afisare: list
      When products: I add product to basket "Telefon mobil Samsung Galaxy S21 FE, Dual SIM, 6GB RAM, 128GB, 5G, White"
      When products: I click Vezi detalii cos

    @cart_price
    Scenario: Test cart total price functionality
      Then cart: I verify that total price is correct "2.649,00 Lei"


    @cart_remove
    Scenario: Test cart remove product functionality
      When cart: I click sterge link
      Then cart: I verify empty cart message is displayed




