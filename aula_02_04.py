from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse



service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

driver.get('http://selenium.dunossauro.live/aula_04_b.html')

url_parseada = urlparse(driver.current_url)
print(url_parseada)


sleep(2)
driver.quit()
