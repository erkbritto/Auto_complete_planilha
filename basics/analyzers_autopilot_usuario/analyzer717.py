from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 94addd17bfc94131881841fa04023188

class Analyzer717 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 8):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("*Digite a opção desejada para atualização*:\n\n1 - E-mail\n2 - Nome\n3 - Endereço\n4 - RG\n5 - Telef")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("Para atualização do telefone, peço que nos envie seu nome completo, CPF, o protocolo deste atendimen")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 7',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
    