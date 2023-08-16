from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from package.get_elements import encontrar_elemento_href
from package.get_elements import encontrar_elemento_texto


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(3)
driver.get('http://selenium.dunossauro.live/aula_04_a.html')


elem_ddg = encontrar_elemento_texto(driver, 'DuckDuckGo', 'a')

if elem_ddg is not None:
    print(elem_ddg.text)

elem_ddg = encontrar_elemento_href(driver, 'ddg')

if elem_ddg is not None:
    print(elem_ddg.get_attribute('href'))

time.sleep(1)
driver.quit()
