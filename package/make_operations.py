from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


def find_answer_options(driver, element, answer, normal=True):
    """
    Encontra e seleciona a opção de resposta desejada em uma lista de opções.

    Args:
        driver (WebDriver): O webdriver do Selenium configurado.
        element (str): O nome da tag HTML que contém a lista de opções.
        answer (str): O texto da âncora da opção de resposta desejada.
        normal (bool, optional): Define o modo de seleção. 
            Se True (padrão), a opção de resposta com o texto correspondente
            será selecionada. Se False, a opção de resposta com 
            texto diferente será selecionada.
    Returns:
        None
    """
    tag = driver.find_element(By.TAG_NAME, element)

    elements = tag.find_elements(By.TAG_NAME, 'li')

    for _element in elements:
        a = _element.find_element(By. TAG_NAME, 'a')

        if normal:
            if a.text == answer:
                a.click()
                break
        else:
            if a.text != answer:
                a.click()
                break


def enviar_detalhes_filme(driver, nome, email, telefone):
    """
    Preenche e envia os detalhes de um filme.

    Esta função utiliza um driver para interagir com uma página da web e preencher
    os campos necessários com informações sobre um filme, incluindo nome, email e telefone.
    Após o preenchimento, ela clica no botão de envio correspondente.

    Args:
        driver: Instância do driver para interação com a página da web.
        nome (str): O nome do filme a ser inserido.
        email (str): O email do usuário para contato.
        telefone (str): O número de telefone do usuário para contato.

    Returns:
        None
    """
    campo_nome = driver.find_element(By.NAME, 'filme')
    campo_email = driver.find_element(By.NAME, 'email')
    campo_telefone = driver.find_element(By.NAME, 'telefone')
    botao_enviar = driver.find_element(By.NAME, 'enviar')

    campo_nome.send_keys(nome)
    campo_email.send_keys(email)
    campo_telefone.send_keys(telefone)
    botao_enviar.click()


def preencher_formulario(driver, nome, email, senha, telefone):
    """
    Preenche um formulário com informações fornecidas e realiza o envio.

    Esta função utiliza um driver para interagir com um formulário em uma página da web.
    Ela preenche os campos de nome, email, senha e telefone com as informações fornecidas.
    Após o preenchimento, a função clica no botão de envio correspondente.

    Args:
        driver: Instância do driver para interação com a página da web.
        nome (str): O nome a ser inserido no campo de nome.
        email (str): O email a ser inserido no campo de email.
        senha (str): A senha a ser inserida no campo de senha.
        telefone (str): O número de telefone a ser inserido no campo de telefone.

    Returns:
        None
    """
    campo_nome = driver.find_element(By.NAME, 'nome')
    campo_email = driver.find_element(By.NAME, 'email')
    campo_senha = driver.find_element(By.NAME, 'senha')
    campo_telefone = driver.find_element(By.NAME, 'telefone')
    botao_enviar = driver.find_element(By.NAME, 'btn')

    campo_nome.send_keys(nome)
    campo_email.send_keys(email)
    campo_senha.send_keys(senha)
    campo_telefone.send_keys(telefone)
    botao_enviar.click()

if __name__ == "__main__":
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)
    driver.get('https://selenium.dunossauro.live/exercicio_03.html')

    find_answer_options(driver, 'main', 'Começar por aqui')

    sleep(2)
    driver.quit()