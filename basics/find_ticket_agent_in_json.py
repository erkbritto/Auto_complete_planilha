
from basics.JsonDataHandler import JsonDataHandler
from typing import List
from basics.find_ticket_by_id import Message

# Instancia a classe para lidar com os dados salvos em JSON
jsonDataHandler = JsonDataHandler('output/agent-chats.json')

# Carregando dados do JSON
messageDictionary = jsonDataHandler.load_data()

def find_ticket_agent_in_json(interactionId:str) -> List[Message]:
    
    # Verifica se o interactionId existe no JSON e retorna as mensagens do chat
    if not interactionId in messageDictionary:
        raise Exception('interactionId not found', interactionId)

    chats = messageDictionary[interactionId]
    
    return chats
