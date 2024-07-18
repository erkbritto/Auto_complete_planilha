from basics.get_file_name import get_file_name
from basics.find_ticket_by_id import find_ticket_by_id
from basics.helper_xlsx import HelperXlsx, INTERACTION_ID, OPCAO_SELECIONADA, JORNADA_DO_CLIENTE_NO_CHATBOT, FINALIZACAO_DO_CONTATO
from basics.get_token import get_token
from basics.JsonDataHandler import JsonDataHandler

# Obtém o nome do arquivo
fileName:str = get_file_name()

# Obtendo token
get_token()

# Instancia a classe para lidar com o xlsx
helperXlsx = HelperXlsx()


# Instancia a classe para lidar com os dados salvos em JSON
jsonDataHandler = JsonDataHandler('output/chats.json')

# Carregando dados do JSON
messageDictionary = jsonDataHandler.load_data()

# Ler os dados do arquivo xlsx
file = helperXlsx.read(fileName)

# Pular a primeira linha
for index, line in enumerate(file):

    # Imprime o progresso
    print(f"{index}/{len(file)}")

    # pula o titulo
    if index == 0:
        continue
    
    # pula os vazios
    if not line[INTERACTION_ID]:
        continue
    
    # Forma de obter(e definir os dados do ticket)
    messages = find_ticket_by_id(line[INTERACTION_ID])
    
    # insere as mensagens no arquivo JSON
    messageDictionary[line[INTERACTION_ID]] = messages

    # Salva os dados no JSON a cada iteração
    jsonDataHandler.save_data(messageDictionary)

# Salva os dados no JSON no fim da execução
jsonDataHandler.save_data(messageDictionary)
