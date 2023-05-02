Feature: Emag favorites feature

  Background:
    Given home: I am a user on emag.ro Home page

  @favorites
  Scenario: Click on a favorite product, then from favorite cart we will add to cart the product and delete from favorites
    When home: I hover over "Laptop, Tablete & Telefoane"
    When home: I click subcategory "Laptopuri"
    When home: I click Tip afisare: list
    When favorite: I add to favorites cart the laptop "Laptop HP 15s-fq3018nq"
    When favorite: I click on Produse Favorite
    When favorite: I check that i have reached the favorites page url
    When favorite: I click on the button Add to Basket from Favorites "Laptop HP 15s-fq3018nq"
    And favorite: I check the message on the basket to see that it has been added "1"
    Then favorite: I click on the delete buton from Favorites "Laptop HP 15s-fq3018nq"