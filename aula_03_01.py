from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pprint import pprint


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

url = 'http://selenium.dunossauro.live/aula_05_a.html'

driver.get(url)

div_python = driver.find_element(By.ID, 'python')
pprint(div_python.text)

div_haskell = driver.find_element(By.ID, 'haskell')
pprint(div_haskell.text)

sleep(1)
driver.quit()