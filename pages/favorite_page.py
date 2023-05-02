from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FavoritePage(BasePage):
    # Atributs
    PRODUSE_FAVORITE_BTN = (By.ID, "my_wishlist")

    # Methods
    def add_to_favorites_by_product_name(self, name):
        self.wait_scroll_and_click_elem_by_selector(By.XPATH, '//i[@class="em em-fav em-fav-bold"]')

    def delete_from_favorites_by_product_name(self, name):
        self.wait_and_click_elem_by_selector(By.XPATH, '//i[@class="em em-delete gtm_9p2y1a"]')
            #                                    //span[@class="hidden-sm hidden-xs gtm_9p2y1a"]
    def click_produse_favorite(self):
        self.wait_and_click_elem_by_selector(*self.PRODUSE_FAVORITE_BTN)
        sleep(6)

    def add_to_basket_by_name_but_from_favorites_list(self, name):
        self.wait_and_click_elem_by_selector(By.XPATH, '//button[text()="Adauga in Cos"]')

    def check_product_in_cart(self, quantity_cart):
        self.verify_text_on_elem_by_selector(By.XPATH, f'//span[text()="{quantity_cart}"]', '1')

    def verify_favorites_url(self):
        self.verify_page_url('https://www.emag.ro/favorites?ref=ua_favorites')


