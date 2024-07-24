from basics.helper_xlsx import HelperXlsx, INTERACTION_ID, OPCAO_SELECIONADA, JORNADA_DO_CLIENTE_NO_CHATBOT, FINALIZACAO_DO_CONTATO, ANALYZER_ID
from basics.get_file_name import get_file_name
from basics.find_ticket_in_json import find_ticket_in_json
from basics.find_ticket_agent_in_json import find_ticket_agent_in_json
from basics.getAnalyzers2 import getAnalyzers

fileName: str = get_file_name()

# Instancia a classe para lidar com o xlsx
helperXlsx = HelperXlsx()

# Ler os dados do arquivo xlsx
file = helperXlsx.read(fileName)

# Pular a primeira linha
for index, line in enumerate(file):
    
    if index == 0:
        continue

    # Forma de obter (e definir os dados do ticket)
    messagesBot = find_ticket_in_json(line[INTERACTION_ID])
    messagesclient = find_ticket_in_json(line[INTERACTION_ID])

    # Pula linhas onde INTERACTION_ID está vazio
    if not line[INTERACTION_ID]:
        continue

    # Instancia os analisadores
    analyzers = getAnalyzers()
    
    for analyzerId, analyzer in enumerate(analyzers):
        # Incrementa o id do analyzer
        analyzerId += 1

        # Pula caso a estrutura não seja válida para messagesBot e messagesclient
        if not analyzer.isValid(messagesBot, messagesclient):
         continue

    
        # Pega as qualificações
        qualifications = analyzer.getQualifications(messagesBot, messagesclient)
        qualificationsclient = analyzer.getQualifications(messagesBot, messagesclient)

        # Insere as qualificações no ticket
        file[index][OPCAO_SELECIONADA] = qualifications['selectedOption']
        file[index][JORNADA_DO_CLIENTE_NO_CHATBOT] = qualifications['customerJourney']
        file[index][FINALIZACAO_DO_CONTATO] = qualifications['finalizationOfTheContract']
        file[index][ANALYZER_ID] = analyzerId

        # Encerra o loop dos analisadores caso o ticket tenha sido validado
        break

# Salva o arquivo no fim da execução
helperXlsx.write('./output/file2.xlsx', file)

from basics.JsonDataHandler import JsonDataHandler
from typing import List
from basics.find_ticket_by_id import Message

# Instancia a classe para lidar com os dados salvos em JSON
jsonDataHandler = JsonDataHandler('output/chats.json')

# Carregando dados do JSON
messageDictionary = jsonDataHandler.load_data()

def find_ticket_in_json(interactionId: str) -> List[Message]:
    # Verifica se o interactionId existe no JSON e retorna as mensagens do chat
    if not interactionId in messageDictionary:
        print(f"interactionId not found: {interactionId}")
        print("Available IDs:", list(messageDictionary.keys()))  # Mostra IDs disponíveis
        raise Exception('interactionId not found', interactionId)

    chats = messageDictionary[interactionId]
    
    return chats

