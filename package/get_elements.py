from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
import time

def encontrar_elemento_href(browser, link):
    """
    Localiza o primeiro elemento âncora que contém o link especificado em seu atributo href.

    Esta função utiliza um navegador (browser) para encontrar elementos âncora na página da web
    que contenham o link especificado em seu atributo href. Ela itera sobre os elementos encontrados
    e retorna o primeiro elemento cujo atributo href contém o link fornecido.

    Args:
        browser: Instância do navegador para interação com a página da web.
        link (str): O link a ser procurado no atributo href dos elementos âncora.

    Returns:
        element: O primeiro elemento âncora que contém o link no atributo href, ou None se não for encontrado.
    """
    elementos = browser.find_elements(By.TAG_NAME, 'a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento
    return None


def encontrar_elemento_texto(browser, texto, tag):
    """
    Localiza o primeiro elemento que corresponde ao texto especificado e à tag fornecida.

    Esta função utiliza um navegador (browser) para encontrar elementos na página da web
    que correspondem ao texto e à tag especificados. Ela itera sobre os elementos encontrados
    e retorna o primeiro elemento cujo texto coincide com o texto fornecido.

    Args:
        browser: Instância do navegador para interação com a página da web.
        texto (str): O texto a ser procurado nos elementos.
        tag (str): A tag HTML dos elementos a serem pesquisados.

    Returns:
        element: O primeiro elemento que corresponde ao texto e à tag, ou None se não for encontrado.
    """
    elementos = browser.find_elements(By.TAG_NAME, tag)

    for elemento in elementos:
        if elemento.text == texto:
            return elemento
    return None


def get_all_links(driver, url, timeout=10):
    """
    Coleta os links de navegação de uma página da web usando o Selenium.

    Args:
        driver (WebDriver): O driver do Selenium para controle do navegador.
        url (str): A URL da página da web a ser analisada.
        timeout (int, opcional): O tempo máximo de espera 
            para carregamento dos elementos. O padrão é 10 segundos.

    Returns:
        dict: Um dicionário contendo os textos dos links como chaves 
            e os URLs como valores.
    """
    try:
        driver.get(url)

        condicion = EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
        WebDriverWait(driver, timeout).until(condicion)

        elementos = driver.find_elements(By.TAG_NAME, 'a')

        links_dict = {
            elemento.text: elemento.get_attribute('href') 
            for elemento in elementos
        }

    except TimeoutException:
        print("Tempo limite excedido ao carregar a página.")

    finally:

        driver.quit()

    return links_dict


def get_links(driver, url, element, timeout=10):
    """ 
    Coleta os links de navegação de uma página da web usando o Selenium.
    
    Esta função utiliza um webdriver Selenium para acessar a URL fornecida e
    extrair os links de âncoras encontrados nos elementos especificados.

    Args:
        driver (WebDriver): O webdriver do Selenium configurado.
        url (str): A URL da página da web a ser acessada.
        element (str): O nome da tag HTML que contém os links de âncoras.
        timeout (int, optional): O tempo máximo (em segundos) a aguardar 
            até que os elementos estejam presentes. O valor padrão é 10.

    Returns:
        dict: Um dicionário contendo os textos das âncoras como chaves 
            e os URLs correspondentes como valores.
    """

    try:
        result = {}

        driver.get(url)

        condicion = EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
        WebDriverWait(driver, timeout).until(condicion)

        _elements = driver.find_elements(By.TAG_NAME, element)
        ancoras = _elements.find_elements(By.TAG_NAME, 'a')

        result = {
            ancora.text: ancora.get_attribute('href') 
            for ancora in ancoras
        }

    except TimeoutException:
        print("Tempo limite excedido ao carregar a página.")

    finally:

        driver.quit()

    return result

if __name__ == "__main__":
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver_2 = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    url = 'http://google.com'

    links = get_all_links(driver, url)
    pprint(links['Gmail'])

    time.sleep(5)
    driver_2.quit()
    
