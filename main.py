from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def ler_ids_do_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        ids = file.read().splitlines()
    return ids

def fazer_login(driver, url, username, password):
    driver.get(url)
    
        # Aguarde o carregamento da próxima página
    time.sleep(15)  # Ajuste conforme necessário


    # Inserir o e-mail
    campo_email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    campo_email.send_keys(username)

    # Inserir a senha
    campo_senha = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    campo_senha.send_keys(password)

    # Clicar no botão de login
    botao_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    botao_login.click()

    # Aguarde o carregamento da próxima página
    time.sleep(15)  # Ajuste conforme necessário

def pesquisar_id(driver, id):
    # Construir a URL com o ID
    url = f"https://jobhomeniodigital.mytalkdesk.com/atlas/apps/virtual-agent/sessionMonitor?dateRangeOption=last30days&escalated=true&type=ARCHIVED&interactionId={id}&selectedPage=1"
    
    driver.get(url)
    time.sleep(15)  # Ajuste conforme necessário

    # Clicar na div com data-co-name="avatar"
    div_avatar = driver.find_element(By.CSS_SELECTOR, "div[data-co-name='avatar']")
    div_avatar.click()
    time.sleep(2)  # Aguarde a ação ser processada




    # Coletar os resultados. Adapte conforme necessário.
    opcao1 = driver.find_element(By.CSS_SELECTOR, "SELETOR_CSS_DA_OPCAO1").text
    opcao2 = driver.find_element(By.CSS_SELECTOR, "SELETOR_CSS_DA_OPCAO2").text
    opcao3 = driver.find_element(By.CSS_SELECTOR, "SELETOR_CSS_DA_OPCAO3").text

    return opcao1, opcao2, opcao3

def salvar_resultados(caminho_arquivo, resultados):
    with open(caminho_arquivo, 'w') as file:
        for resultado in resultados:
            file.write(';'.join(resultado) + '\n')

def main():
    caminho_arquivo_ids = r'C:\temp\ids.txt'  # Arquivo com os IDs para pesquisar
    caminho_arquivo_resultados = r'C:\temp\resultados.txt'  # Arquivo onde salvar os resultados

    ids = ler_ids_do_arquivo(caminho_arquivo_ids)

    # Defina suas credenciais
    url_login = "https://jobhomeniodigital.talkdeskid.com/login"
    username = "edy.alves@jobhome.com.br"  # Substitua com seu nome de usuário
    password = "Jobhome1010"  # Substitua com sua senha

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Faça login
    fazer_login(driver, url_login, username, password)

    # Pesquisar IDs após login
    resultados = []
    for id in ids:
        opcao1, opcao2, opcao3 = pesquisar_id(driver, id)
        resultados.append((id, opcao1, opcao2, opcao3))

    driver.quit()

    salvar_resultados(caminho_arquivo_resultados, resultados)

if __name__ == "__main__":
    main()
