from selenium.webdriver.common.by import By
import time
import os

def login(driver):

    # Defina suas credenciais
    username = os.environ.enEMAIL  # Substitua com seu nome de usuário
    password = os.environ.enPASS  # Substitua com sua senha

    # Defina suas credenciais    
    url = "https://jobhomeniodigital.talkdeskid.com/login"

    driver.get(url)
    
    # Aguarde o carregamento da próxima página
    time.sleep(15)

    # Inserir o e-mail
    email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_field.send_keys(username)

    # Inserir a senha
    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_field.send_keys(password)

    # Clicar no botão de login
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Aguarde o carregamento da próxima página
    time.sleep(15)  # Ajuste conforme necessário
