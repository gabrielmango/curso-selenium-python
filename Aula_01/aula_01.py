from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(3)

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
driver.get(url)

a = driver.find_element(By.TAG_NAME, 'a')
valor_click = 0
for click in range(10):
    ps = driver.find_elements(By.TAG_NAME, 'p')
    a.click()
    print(f'Valor do último p: {ps[-1].text}, valor do click: {click}')
    valor_click = click

if int(ps[-1].text) == valor_click:
    print('Os valores são iguais')

sleep(1)
driver.quit()
