from behave import *




@when('my_account: I click my account button')
def step_impl(context):
    context.my_account_page.click_my_account_btn()

@when('my_account: I click on vezi istoricul de comenzi')
def step_impl(context):
    context.my_account_page.click_my_orders_btn()



@then('my_account: I verify my account page url')
def step_impl(context):
    context.my_account_page.verify_my_account_url()

