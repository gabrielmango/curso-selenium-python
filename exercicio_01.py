"""
Exercício 01: 

Criar um programa com Selenium que gere um dicionário, onde a chave é a tag h1
- O valor deve ser um novo dicionário
- Cada chave do valor deverá ser o valor de 'atributo'
- Cada valor deverá ser o texto contido no elemento

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pprint import pprint

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(3)

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
driver.get(url)
elements = driver.find_elements(By.TAG_NAME, 'p')

dic_h1 = dict()
dicionario = dict()

for element in elements:
    dic_h1[element.get_attribute('atributo')] = element.text
driver.quit()

dicionario['H1'] = dic_h1
pprint(dicionario)