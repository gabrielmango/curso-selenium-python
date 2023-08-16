from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

url = 'http://selenium.dunossauro.live/aula_04_a.html'
driver.get(url)

uls = driver.find_elements(By.TAG_NAME, 'ul')

lis = uls[0].find_elements(By.TAG_NAME, 'li')

for li in lis:
    a = li.find_element(By.TAG_NAME, 'a')
    print(a.text)


time.sleep(1)
driver.quit()
