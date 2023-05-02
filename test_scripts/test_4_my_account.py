from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

# define chrome as a browser, maximize windows and open the url
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://emag.ro')

# click pe Contul meu
driver.find_element(By.ID, 'my_account').click()
sleep(4)

# verificam ca ne-a redirectionat catre pagina de login
assert driver.current_url == 'https://auth.emag.ro/user/login'

#introducem adresa de email in input ul de email:
driver.find_element(By.ID, 'user_login_email').send_keys('test_emag_itf@yopmail.com')
sleep(15)

#introducem parola in input ul de parola:
driver.find_element(By.ID, 'user_login_password').send_keys('Test1234@')
sleep(15)

# click pe continua pentru logare in cont
driver.find_element(By.ID, 'user_login_continue').click()
sleep(15)

# verificam ca ne-a redirectionat catre pagina de Autentificare multi-factor
assert driver.current_url == 'https://www.emag.ro/user/mfa-optin'

# click pe continua pe Activează mai târziu
driver.find_element(By.XPATH, '//*[text()="Activează mai târziu"]').click()
sleep(3)

# verificam ca ne-am autentificat:
# hover pe contul meu:
contul_meu = driver.find_element(By.CLASS_NAME, 'span.ini')
hover = ActionChains(driver).move_to_element(contul_meu)
hover.perform()
# verificam mesajul de salut din contul meu:
username_test = driver.find_element(By.XPATH, "//strong[text()='Salut, test emag itf']")
assert username_test == 'Salut, test emag itf'
sleep(3)

# verificam pagina url pentru contul meu:
assert driver.current_url == 'https://www.emag.ro/user/myaccount?ref=ua_personal_data'

