from selenium.webdriver.common.by import By
import time

def findAgentChat(driver, id):
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