from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyAccountPage(BasePage):
    # Attributes
    MY_ACCOUNT_BTN = (By.CLASS_NAME, 'span.ini')
    MY_ORDERS_BTN = (By.XPATH, '//li[@class="is-active"]')
    USERNAME_MSG = (By.XPATH, "//strong[text()='Salut, test emag itf']")
    # Methods

    def click_my_account_btn(self):
        self.wait_and_click_elem_by_selector(*self.MY_ACCOUNT_BTN)

    def verify_username_msg(self, expected_username_msg):
        self.wait_and_click_elem_by_selector(*self.USERNAME_MSG)
        actual_username_msg = self.driver.find_element(*self.USERNAME_MSG).text
        self.assertEqual(actual_username_msg, expected_username_msg,
        f"Incorrect username msg: expected = {expected_username_msg} but actual = {actual_username_msg}")

    def click_my_orders_btn(self):
        self.wait_and_click_elem_by_selector(*self.MY_ORDERS_BTN)



    def verify_my_account_url(self):
        self.verify_page_url('https://www.emag.ro/user/myaccount?ref=ua_personal_data')






