from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pprint import pprint
from package.make_operations import enviar_detalhes_filme


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

url = 'http://selenium.dunossauro.live/aula_05_c.html'

driver.get(url)

enviar_detalhes_filme(driver, 'Parasita', 'teste@teste.tst', '(000)987654321')


sleep(2)
driver.quit()