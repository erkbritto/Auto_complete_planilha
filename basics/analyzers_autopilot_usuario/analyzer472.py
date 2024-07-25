from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# e538c0c42519444b8365d5e9a8c434a6

class Analyzer472 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 30):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("Digite:\n\n1 - Dificuldade em efetuar compras com o cartão.\n2 - Outros assuntos.\n3 - Retornar ao m")):
            return False
    
        if not (messagesClient[9]["sender"] == "bot" and messagesClient[9]["message"].startswith("Desculpe, não entendi sua solicitação, por favor, tente novamente Digite:\n\n1 - Dificuldade em efet")):
            return False
    
        if not (messagesClient[11]["sender"] == "bot" and messagesClient[11]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[13]["sender"] == "bot" and messagesClient[13]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[15]["sender"] == "bot" and messagesClient[15]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesClient[17]["sender"] == "bot" and messagesClient[17]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[19]["sender"] == "bot" and messagesClient[19]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[21]["sender"] == "bot" and messagesClient[21]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[23]["sender"] == "bot" and messagesClient[23]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesClient[25]["sender"] == "bot" and messagesClient[25]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[27]["sender"] == "bot" and messagesClient[27]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[29]["sender"] == "bot" and messagesClient[29]["message"].startswith("Para registrar elogios, sugestões ou reclamações, acesso o nosso site www.niodigital.com.br e efetue")):
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
    