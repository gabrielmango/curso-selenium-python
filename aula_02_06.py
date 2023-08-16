from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pprint import pprint

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

url = 'http://selenium.dunossauro.live/aula_04.html'

driver.get(url)

a_tags = driver.find_elements(By.TAG_NAME, 'a')

links_aulas = dict()
links_exercicios = dict()
links_navegacao = dict()

for a in a_tags:
    if 'Aula' in a.text:
        links_aulas[a.text] = a.get_attribute('href')
    elif 'Exercício' in a.text:
        links_exercicios[a.text] = a.get_attribute('href')
    else:
        links_navegacao[a.text] = a.get_attribute('href')

sleep(1)
driver.quit()

print()
pprint(links_aulas)
pprint(links_exercicios)
pprint(links_navegacao)




