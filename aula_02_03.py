from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from aula_02_02 import find_by_text


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

driver.get('http://selenium.dunossauro.live/aula_04_b.html')

nomes_caixas = ['um', 'dois', 'tres', 'quatro']
for nome in nomes_caixas:
    time.sleep(1)   
    find_by_text(driver, nome, 'div').click()

for nome in nomes_caixas:
    time.sleep(1)   
    driver.back()

for nome in nomes_caixas:
    time.sleep(1)   
    driver.forward()

time.sleep(2)
driver.quit()
