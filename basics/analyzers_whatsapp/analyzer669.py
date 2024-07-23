from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# b41d3737f3bc40fbb49c228c3bd70921

class Analyzer669 :

    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 22):
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
    
        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("O valor mínimo é de R$0.00, e será descontado automaticamente em folha de pagamento.\nPara efetuar o")):
            return False
    
        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("Aqui está a sua última fatura disponível:\n\nhttps://storage.googleapis.com/bucktgwtalkdesknio/b6123")):
            return False
    
        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesBot[17]["sender"] == "bot" and messagesBot[17]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesBot[19]["sender"] == "bot" and messagesBot[19]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesBot[21]["sender"] == "bot" and messagesBot[21]["message"].startswith("Só um momento que vou transferir para um dos nossos especialistas que irá lhe auxiliar com sua solic")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 6 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }
    