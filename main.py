from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from basics.login import login
from basics.helper_xlsx import HelperXlsx, INTERACTION_ID

def main():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Faça login
    login(driver)

    # Instancia a classe para lidar com o xlsx
    helperXlsx = HelperXlsx()

    # Ler os dados do arquivo xlsx
    file = helperXlsx.read('./input/End of interaction not escaled.xlsx')

    for line in file:
        
        # Forma de obter(e definir os dados do ticket)
        interaction_id = line[INTERACTION_ID]
        # line[OPCAO_SELECIONADA] = "value"
        # line[JORNADA_DO_CLIENTE_NO_CHATBOT] = "value"
        # line[FINALIZACAO_DO_CONTATO] = "value"
        print(interaction_id)
        
        # Insira aqui o código para buscar o ticket
        
        # insira aqui o código para inserir as qualificações no ticket

    # Salva o arquivo
    helperXlsx.write('./output/End of interaction not escalated_updated.xlsx', file)

main()
