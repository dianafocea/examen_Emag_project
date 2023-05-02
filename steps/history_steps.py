from behave import *


@when('history: I click on comenzile mele')
def step_impl(context):
    context.history_page.click_my_orders_btn()

@when('history: I click vezi toate comenzile dropdown')
def step_impl(context):
    context.history_page.click_all_orders_dropdown()
    context.history_page.click_all_orders_dropdown_value()


@when('history: I click din toate dropdown')
def step_impl(context):
    context.history_page.click_all_periods_dropdown()
    context.history_page.click_all_periods_dropdown_value()


@then('history: I can see history page')
def step_impl(context):
    context.history_page.verify_my_orders_url()

