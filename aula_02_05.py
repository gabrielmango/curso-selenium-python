from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)


driver.get('http://selenium.dunossauro.live/aula_04.html')


# Encontra todos os links das aulas
tag_aside = driver.find_element(By.ID, 'aside')
aulas_dict = dict()

aulas = tag_aside.find_elements(By.TAG_NAME, 'li')
for aula in aulas:
    a = aula.find_element(By.TAG_NAME, 'a')
    aulas_dict[a.text] = a.get_attribute('href')


# Encontra todos os links dos exercícios
tag_main = driver.find_element(By.ID, 'main')
exercicios_dict = dict()

exercicios = tag_main.find_elements(By.TAG_NAME, 'li')
for exercicio in exercicios:
    a = exercicio.find_element(By.TAG_NAME, 'a')
    exercicios_dict[a.text] = a.get_attribute('href')


# Encontra todos os links da barra de navegação
tag_header = driver.find_element(By.ID, 'header')
navegacao_dict = dict()

terminal_logo = tag_header.find_element(By.CLASS_NAME, 'logo')
a = terminal_logo.find_element(By.TAG_NAME, 'a')
navegacao_dict[a.text] = a.get_attribute('href')

tag_nav = tag_header.find_element(By.TAG_NAME, 'nav')
lis = tag_nav.find_elements(By.TAG_NAME, 'li')
for li in lis:
    a = li.find_element(By.TAG_NAME, 'a')
    navegacao_dict[a.text] = a.get_attribute('href')


sleep(2)
driver.quit()
print()

for chave, valor in aulas_dict.items():
    print(f'{chave}: {valor}')
print()


for chave, valor in exercicios_dict.items():
    print(f'{chave}: {valor}')
print()


for chave, valor in navegacao_dict.items():
    print(f'{chave}: {valor}')
print()

