from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 297a93f8e74247da9ea7277bb472da7b

class Analyzer433 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 16):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("Você já fez o download do nosso aplicativo NIO Digital📲? \nNele, você pode verificar o limite, consu")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[9]["sender"] == "bot" and messagesClient[9]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesClient[11]["sender"] == "bot" and messagesClient[11]["message"].startswith("*Tudo bem. Digite a opção desejada para*:\n\n1 - Valor mínimo da fatura\n2 - Últimas transações\n3 -")):
            return False
    
        if not (messagesClient[13]["sender"] == "bot" and messagesClient[13]["message"].startswith("O valor mínimo é de")):
            return False
    
        if not (messagesClient[15]["sender"] == "bot" and messagesClient[15]["message"].startswith("Não foi possível consultar a sua ultima fatura, a mesma se encontra indisponível no momento.\nㅤ ㅤ\nT")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
    