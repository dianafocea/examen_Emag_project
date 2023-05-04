from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # Attributes
    TOTAL_PRICE_BIG = (By.XPATH, '//p[@class="price order-summary-total-price"]')
    DELETE_LINK = (By.XPATH, '(//button[contains(text(), "Sterge")])[2]')
    EMPTY_CART_MSG = (By.XPATH, '//p[@class="mrg-btm-none"]')
    CHECKOUT_BTN = (By.XPATH, '//a[@class=" btn btn-emag btn-secondary font-size-md btn-block btn-lg gtm_sn11312018"]')


    # Methods
    def verify_total_price(self, expected_price):
        actual_price = self.driver.find_element(*self.TOTAL_PRICE_BIG).text
        self.assertEqual(actual_price, expected_price, f"Price is incorrect: expected = {expected_price} but actual = {actual_price}")


    def click_sterge_link(self):
        self.wait_and_click_elem_by_selector(*self.DELETE_LINK)

    def verify_empty_cart_msg(self):
        self.verify_element_is_displayed_by_selector(*self.EMPTY_CART_MSG)

    def click_checkout_btn(self):
        self.wait_and_click_elem_by_selector(*self.CHECKOUT_BTN)










