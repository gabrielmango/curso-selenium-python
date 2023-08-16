"""
Exercício 03: 

Criar um programa com Selenium que:
- Deve preencher o formulário e enviar;
- Validar os dados preenchidos com os dados salvos do formulário.

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep
from urllib.parse import urlparse
from pprint import pprint
from package.make_operations import preencher_formulario as envia
from json import loads

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(3)
driver.get('https://selenium.dunossauro.live/exercicio_04.html')

dados = {
    'nome': 'Teste',
    'email': 'teste@teste.tst',
    'senha': '#Teste123',
    'telefone': '(000)987654321',
}

envia(driver, **dados)

resultado = driver.find_element(By.TAG_NAME, 'textarea').text
resultado_formatado = resultado.replace('\'', '\"')

dic_resultado = loads(resultado_formatado)

assert dados == dic_resultado

sleep(1)
driver.quit()