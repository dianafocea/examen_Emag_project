from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HistoryPage(BasePage):
    # Atributs
    MY_ORDERS_BTN = (By.XPATH, '(//a[@class="text-dashboard-primary semibold"])[1]')
    EMPTY_HISTORY_MSG = (By.CLASS_NAME, 'p.mrg-sep-sm]')
    SEARCH_COMENZI = (By.XPATH, '(//input[@placeholder="Cauta dupa produs"])[1]')
    TOATE_COMENZILE_DROPDOWN_STATUS = (By.XPATH, '//select[@name="status"]')
    TOATE_COMENZILE_DROPDOWN_VALUE = (By.XPATH, '//option[@value="all"]')
    TOATE_PERIOADELE_DROPDOWN_TIME = (By.XPATH, '//select[@name="time"]')
    TOATE_PERIOADELE_DROPDOWN_VALUE = (By.XPATH, '//option[@value="older"]')



    # Methods
    def click_my_orders_btn(self):
        self.wait_and_click_elem_by_selector(*self.MY_ORDERS_BTN)

    def click_all_orders_dropdown(self):
        self.wait_and_click_elem_by_selector(*self.TOATE_COMENZILE_DROPDOWN_STATUS)

    def click_all_orders_dropdown_value(self):
        self.wait_and_click_elem_by_selector(*self.TOATE_COMENZILE_DROPDOWN_VALUE)

    def click_all_periods_dropdown(self):
        self.wait_and_click_elem_by_selector(*self.TOATE_PERIOADELE_DROPDOWN_TIME)

    def click_all_periods_dropdown_value(self):
        self.wait_and_click_elem_by_selector(*self.TOATE_PERIOADELE_DROPDOWN_VALUE)

    def verify_history_msg(self):
        self.wait_and_click_elem_by_selector(*self.EMPTY_HISTORY_MSG)
        actual = self.driver.find_element(*self.EMPTY_HISTORY_MSG).text
        expected = "Nu ai comenzi plasate in perioada selectata. Te rugam alege o alta perioada."
        assert actual == expected, f"Incorrect history msg: expected = {expected} but actual = {actual}"

    def verify_my_orders_url(self):
        self.verify_page_url('https://www.emag.ro/user/myaccount?ref=ua_personal_data')

