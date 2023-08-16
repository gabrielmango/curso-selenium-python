"""
Exercício 02: 

Criar um programa com Selenium que:
- Jogue o jogo
- Quando você ganhar o script deve parar de ser executado

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from pprint import pprint

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(3)

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
driver.get(url)
a = driver.find_element(By.TAG_NAME, 'a')

contagem = 0

while True:
    a.click()
    contagem += 1
    time.sleep(1)

    elements = driver.find_elements(By.TAG_NAME, 'p')

    if elements[1].text[-1] == elements[-1].text[-1]:
        break

driver.quit()

pprint(f'{contagem} vezes até acertar!')