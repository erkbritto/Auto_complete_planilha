from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 9068c39b746f44e19564e415e1fe7a03

class Analyzer137 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 6):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("Para efetuar o bloqueio do seu cartão, NIO Digital, precisamos que nos forneça a seguinte informação")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 4',
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
    