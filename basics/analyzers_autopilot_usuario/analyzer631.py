from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 8f003894fdc7420fb8eb58fa042946c9

class Analyzer631 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 22):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesClient[9]["sender"] == "bot" and messagesClient[9]["message"].startswith("*Tudo bem. Digite a opção desejada para*:\n\n1 - Valor mínimo da fatura\n2 - Últimas transações\n3 -")):
            return False
    
        if not (messagesClient[11]["sender"] == "bot" and messagesClient[11]["message"].startswith("Já faz mais de 5 dias que efetuou o pagamento da fatura? (Sim ou Não)ㅤ")):
            return False
    
        if not (messagesClient[13]["sender"] == "bot" and messagesClient[13]["message"].startswith("Nesse caso, você deverá aguardar a compensação bancária de 3 a 5 dias úteis. ㅤ\nTe ajudo em algo mai")):
            return False
    
        if not (messagesClient[15]["sender"] == "bot" and messagesClient[15]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[17]["sender"] == "bot" and messagesClient[17]["message"].startswith("Você já fez o download do nosso aplicativo NIO Digital📲? \nNele, você pode verificar o limite, consu")):
            return False
    
        if not (messagesClient[19]["sender"] == "bot" and messagesClient[19]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[21]["sender"] == "bot" and messagesClient[21]["message"].startswith("Para registrar elogios, sugestões ou reclamações, acesso o nosso site www.niodigital.com.br e efetue")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 4 opções do menu',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
    