from basics.find_ticket_by_id import Message
from basics.qualification import FinalizationOfTheContract
from typing import List

def getFinalizationOfTheContract(
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> FinalizationOfTheContract:

    if(len(search_messages(allMessages, "Esperei sua resposta")) == 1):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "Nio Digital agradece o seu contato")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "Por falta de resposta nosso contato será finalizado")) == 1):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "Por falta de interação")) == 1):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "No momento estamos fora do nosso horário de atendimento")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "A NIO agradece seu contato")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "não obtive seu retorno")) == 1):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "Agradecemos muito pelo seu contato")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "Foi um prazer ter te ajudado hoje")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "Esperei sua resposta")) == 1):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "não recebemos sua resposta")) >= 1):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "Por falta de comunicação")) == 1):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "ficamos à disposição")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "A NIO quem agradece seu contato")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "pela compreensão")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "Obrigada pelo seu contato!")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "Por falta de resposta nosso contato será finalizado")) == 1):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "Disponha obrigada ótimo dia")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "Tenha uma ótima tarde")) == 1):
        return 'Contato encerrado com script de finalização.'

    if((len(messagesBot) + 1) == len(allMessages)) and allMessages[-1]["sender"] == 'bot':
        return 'Sem interação - Sem resposta do cliente'

    if('sistema esta indisponivel' in allMessages[-1]['message']):
        return 'Contato encerrado com script de finalização.'

    if('aguarde retorno por favor' in allMessages[-1]['message']):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "estamos à disposição")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(allMessages[-1]['sender'] == 'bot' and ('!' in allMessages[-1]['message'])):
        return 'Contato encerrado com script de finalização.'

    if((allMessages[-1]['sender'] == 'bot') and ('algo mais ?' in allMessages[-1]['message'])):
        return 'Sem interação - Sem resposta do cliente'

    if((allMessages[-1]['sender'] == 'bot') and ('?' in allMessages[-1]['message'])):
        return 'Sem interação - Sem resposta do cliente'

    if(len(search_messages(allMessages, "Tenha um")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "Nio Digital agradece")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "ótima tarde")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(len(search_messages(allMessages, "ótimo dia")) == 1):
        return 'Contato encerrado com script de finalização.'

    if(allMessages[-2]['sender'] == 'client' and allMessages[-2]['message'] == '10'):
        return 'Fatura'

    if all(message['sender'] == 'client' for message in allMessages[len(messagesBot):]):
        return 'Abandono'

    if allMessages[-1]['sender'] == 'bot':
        return 'Sem interação - Sem resposta do cliente'

    if all(message['sender'] == 'client' for message in allMessages[-3:]):
        return 'Abandono'

    if 'algo mais?' in allMessages[-2]['message']:
        return 'Contato encerrado com script de finalização.'

    if (allMessages[-2]['sender'] == 'bot') and ('?' in allMessages[-2]['message']) and (allMessages[-1]['sender'] == 'client'):
        return 'Abandono'

    if (allMessages[-1]['sender'] == 'client' and ('brigad' in allMessages[-1]['message'])):
        return 'Contato encerrado com script de finalização.'

    if(allMessages[-1]['sender'] == 'client' and ('obg' in allMessages[-1]['message'])):
        return 'Contato encerrado com script de finalização.'

    if(allMessages[-1]['sender'] == 'client' and ('Obg' in allMessages[-1]['message'])):
        return 'Contato encerrado com script de finalização.'

    if(allMessages[-1]['sender'] == 'client' and ('Tudo bem' in allMessages[-1]['message'])):
        return 'Contato encerrado com script de finalização.'

    if all(message['sender'] == 'client' for message in allMessages[-2:]):
        return 'Abandono'
    
    if(allMessages[-2]['sender'] == 'bot' and ('aguarde um momento' in allMessages[-2]['message'])) and (allMessages[-1]['sender'] == 'client'):
        return 'Abandono'

    if(allMessages[-2]['sender'] == 'bot' and ('agradeço o contato' in allMessages[-2]['message'])) and (allMessages[-1]['sender'] == 'client'):
        return 'Contato encerrado com script de finalização.'

    if(allMessages[-2]['sender'] == 'bot' and ('m momento' in allMessages[-2]['message'])) and (allMessages[-1]['sender'] == 'client'):
        return 'Abandono'
    
    if(allMessages[-1]['sender'] == 'client' and ('nada' in allMessages[-1]['message'])):
        return 'Contato encerrado com script de finalização.'
   
    if(allMessages[-1]['sender'] == 'client' and ('?' in allMessages[-1]['message'])):
        return 'Abandono'
    
    if(allMessages[-1]['sender'] == 'client'):
        return 'Contato encerrado com script de finalização.'

    return 'not implemented'

def search_messages(messages: List[Message], query: str) -> List[Message]:
    result = []
    for message in messages:
        if query.lower() in message["message"].lower():
            result.append(message)
    return result