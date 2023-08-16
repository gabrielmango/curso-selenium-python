from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
from pprint import pprint
from urllib.parse import urlparse
from package.make_operations import preencher_formulario
from json import loads

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

url = 'http://selenium.dunossauro.live/aula_05.html'

driver.get(url)

dados_preender = {
    'nome': 'Teste formulário',
    'email': 'teste@teste.tst',
    'senha': 'T@este123',
    'telefone': '(000)987654321',
}

preencher_formulario(driver, **dados_preender)

sleep(2)
parsed_url = urlparse(driver.current_url)

texto_resultado = driver.find_element(By.ID, 'result').text
resultado_formatado = texto_resultado.replace('\'', '\"')

pprint(resultado_formatado)

dic_resultado = loads(resultado_formatado)

assert dic_resultado == dados_preender

sleep(5)
driver.quit()