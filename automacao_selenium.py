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