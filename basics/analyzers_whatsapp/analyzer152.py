from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# ae132fdd34854ed09792cca8b9ffaab5

class Analyzer152 :

    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 8):
            return False
    
        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("Para efetuar o bloqueio do seu cartão, NIO Digital, precisamos que nos forneça a seguinte informação")):
            return False
    
        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("Os 4 últimos dígitos inseridos não são validos, vamos transferi-lo para um de nossos agentes.")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 4',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }
    