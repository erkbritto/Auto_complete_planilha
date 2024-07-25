from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 2d14c70bea24469d854b8357f1b72e89

class Analyzer417 :

    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 32):
            return False
    
        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?")):
            return False
    
        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("O últimos 4 dígitos que você digitou está inválido ou não foi possível consultar o limite. Por favor")):
            return False
    
        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?")):
            return False
    
        if not (messagesBot[17]["sender"] == "bot" and messagesBot[17]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesBot[19]["sender"] == "bot" and messagesBot[19]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesBot[21]["sender"] == "bot" and messagesBot[21]["message"].startswith("*Tudo bem. Digite a opção desejada para*:\n\n1 - Valor mínimo da fatura\n2 - Últimas transações\n3 -")):
            return False
    
        if not (messagesBot[23]["sender"] == "bot" and messagesBot[23]["message"].startswith("Não foi possível consultar a sua ultima fatura, a mesma se encontra indisponível no momento.\nㅤ ㅤ\nT")):
            return False
    
        if not (messagesBot[25]["sender"] == "bot" and messagesBot[25]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesBot[27]["sender"] == "bot" and messagesBot[27]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesBot[29]["sender"] == "bot" and messagesBot[29]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adiciona")):
            return False
    
        if not (messagesBot[31]["sender"] == "bot" and messagesBot[31]["message"].startswith("Só um momento enquanto te transferimos para um de nossos agentes.")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 5 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }
    