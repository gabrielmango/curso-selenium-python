"""
Exercício 03: 

Criar um programa com Selenium que:
- Encontre o unicórnio.

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from pprint import pprint
from package.make_operations import find_answer_options


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(3)
driver.get('https://selenium.dunossauro.live/exercicio_03.html')


# Primeiro passo: clicar no botão 
find_answer_options(driver, 'main', 'Começar por aqui')


# Segundo passo: escolher a opção errada 
tag_main = driver.find_element(By.TAG_NAME, 'main')
elements_p = tag_main.find_elements(By.TAG_NAME, 'p')
operacao = elements_p[-1].text.split()
resultado = int(operacao[0]) * int(operacao[2])
find_answer_options(driver, 'main', str(resultado), normal=False)


# Terceiro passo: encontrar o titulo da página
find_answer_options(driver, 'main', driver.title)

        
# Quarto passo: encontrar o path da url atual
url_parseada = urlparse(driver.current_url)
find_answer_options(driver, 'main', url_parseada.path[1:])


# Quint passo: atualizar a página
driver.refresh()


# Unicónio
uniconio = driver.find_element(By.TAG_NAME, 'pre')
pprint(uniconio.text)


sleep(1)
driver.quit()