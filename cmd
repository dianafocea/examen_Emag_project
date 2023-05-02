# Libraries required for installation:
pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager


# We run tests one by one:
behave -f html -o behave-cart-price.html --tags=cart_price
behave -f html -o behave-cart-remove.html --tags=cart_remove
behave -f html -o behave-favorites.html --tags=favorites
behave -f html -o behave-login-test.html --tags=login_test
behave -f html -o behave-login-account.html --tags=login_account
behave -f html -o behave-login-buy.html --tags=login_buy
behave -f html -o behave-logout.html --tags=logout
behave -f html -o behave-search-query.html --tags=search_query
behave -f html -o behave-search-filter.html --tags=search_with_filter
behave -f html -o behave-history.html --tags=history_orders

# We run full test:
behave -f html -o behave-report.html