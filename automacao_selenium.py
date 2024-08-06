# Importando webdriver e By da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# Importando biblioteca time para adicionar uma pausa no nosso codigo
from time import sleep

# Abrindo o navegador para começar a automacação, utilizando o webdriver
chrome = webdriver.Chrome()
# Abrindo uma url
chrome.get('https://www.saucedemo.com/')

#Adicionando uma pausa na execução do codigo
sleep(1)

#Buscando o elemento de input de username utilizando o xpath
input_username = chrome.find_element(By.XPATH, '//input[@id="user-name"]')
#Inserindo o valor no campo de username
input_username.send_keys('standard_user')

#Buscando o elemento de input de password utilizando o xpath
input_password = chrome.find_element(By.XPATH, '//input[@id="password"]')
#Inserindo o valor no campo de password
input_password.send_keys('secret_sauce')

#Buscando o elemento botao de login utilizando o xpath
btn_login = chrome.find_element(By.XPATH, '//input[@id="login-button"]')
#Clicando no elemento
btn_login.click()
sleep(1)

btn_comprar_item = chrome.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
btn_comprar_item.click()

btn_carrinho = chrome.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
btn_carrinho.click()
sleep(1)

btn_checkout = chrome.find_element(By.XPATH, '//button[@id="checkout"]')
btn_checkout.click()
sleep(1)

input_name = chrome.find_element(By.XPATH, '//input[@id="first-name"]')
input_name.send_keys('Giovanni')

input_lastname = chrome.find_element(By.XPATH, '//input[@id="last-name"]')
input_lastname.send_keys('Rodrigues')

input_zip_code = chrome.find_element(By.XPATH, '//input[@id="postal-code"]')
input_zip_code.send_keys('13458500')

btn_continue = chrome.find_element(By.XPATH, '//input[@id="continue"]')
btn_continue.click()
sleep(1)

btn_finish = chrome.find_element(By.XPATH, '//button[@id="finish"]')
btn_finish.click()

sleep(10)