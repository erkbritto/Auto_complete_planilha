from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 01e745751d6640ffb78aa72f0c199d49

class Analyzer831 :

    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 18):
            return False
    
        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?")):
            return False
    
        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("*Tudo bem. Digite a opção desejada para*:\n\n1 - Valor mínimo da fatura\n2 - Últimas transações\n3 -")):
            return False
    
        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("Aqui está a sua última fatura disponível:\n\nhttps://storage.googleapis.com/bucktgwtalkdesknio/21e0c")):
            return False
    
        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("Digite:\n\n1 - Dificuldade em efetuar compras com o cartão.\n2 - Outros assuntos.\n3 - Retornar ao m")):
            return False
    
        if not (messagesBot[17]["sender"] == "bot" and messagesBot[17]["message"].startswith("Só um momento enquanto te transferimos para um de nossos agentes.")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 4 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }
    