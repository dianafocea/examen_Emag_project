from pages.history_page import HistoryPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.favorite_page import FavoritePage
from browser import Browser

# this runs before each test
def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login_page = LoginPage()
    context.product_page = ProductsPage()
    context.cart_page = CartPage()
    context.favorite_page = FavoritePage()
    context.my_account_page = MyAccountPage()
    context.history_page = HistoryPage()



# this runs after the test
def after_all(context):
    context.browser.close()