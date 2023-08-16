from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pprint import pprint


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

url = 'http://selenium.dunossauro.live/aula_05_b.html'

driver.get(url)

topico = driver.find_element(By.CLASS_NAME, 'topico')
pprint(topico.text)
print()

linguagens = driver.find_elements(By.CLASS_NAME, 'linguagens')

for linguagem in linguagens:
    print(
        linguagem.find_element(By.TAG_NAME, 'h2').text,
        linguagem.find_element(By.TAG_NAME, 'p').text
    )

sleep(1)
driver.quit()