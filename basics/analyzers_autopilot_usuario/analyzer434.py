from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 8b249f7f28004d0c8341e6d5b55fe384

class Analyzer434 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 20):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("O últimos 4 dígitos que você digitou está inválido ou não foi possível consultar o limite. Por favor")):
            return False
    
        if not (messagesClient[9]["sender"] == "bot" and messagesClient[9]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesClient[11]["sender"] == "bot" and messagesClient[11]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[13]["sender"] == "bot" and messagesClient[13]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesClient[15]["sender"] == "bot" and messagesClient[15]["message"].startswith("*Tudo bem. Digite a opção desejada para*:\n\n1 - Valor mínimo da fatura\n2 - Últimas transações\n3 -")):
            return False
    
        if not (messagesClient[17]["sender"] == "bot" and messagesClient[17]["message"].startswith("Já faz mais de 5 dias que efetuou o pagamento da fatura? (Sim ou Não)ㅤ")):
            return False
    
        if not (messagesClient[19]["sender"] == "bot" and messagesClient[19]["message"].startswith("Olha, no momento não consta pagamento em nosso sistema.\nPeço que nos envie seu nome completo, CPF, ")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": '',
        }
    