from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 0d8ce390621b41ea95fb5085bb5fa84c

class Analyzer626 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 36):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("Seguem as informações solicitadas")):
            return False
    
        if not (messagesClient[9]["sender"] == "bot" and messagesClient[9]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[11]["sender"] == "bot" and messagesClient[11]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adiciona")):
            return False
    
        if not (messagesClient[13]["sender"] == "bot" and messagesClient[13]["message"].startswith("Para efetuar o desbloqueio do seu cartão, NIO Digital, precisamos que nos forneça algumas informaçõe")):
            return False
    
        if not (messagesClient[15]["sender"] == "bot" and messagesClient[15]["message"].startswith("Qual o nome completo da sua mãe?")):
            return False
    
        if not (messagesClient[17]["sender"] == "bot" and messagesClient[17]["message"].startswith("Qual a sua data de nascimento? (dd/mm/aaaa)")):
            return False
    
        if not (messagesClient[19]["sender"] == "bot" and messagesClient[19]["message"].startswith("Cartão desbloqueado com sucesso.\n💻 Acesse o nosso site e cadastre a sua senha:\nhttps://niodigital.")):
            return False
    
        if not (messagesClient[21]["sender"] == "bot" and messagesClient[21]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[23]["sender"] == "bot" and messagesClient[23]["message"].startswith("Para registrar elogios, sugestões ou reclamações, acesso o nosso site www.niodigital.com.br e efetue")):
            return False
    
        if not (messagesClient[25]["sender"] == "bot" and messagesClient[25]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[27]["sender"] == "bot" and messagesClient[27]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adiciona")):
            return False
    
        if not (messagesClient[29]["sender"] == "bot" and messagesClient[29]["message"].startswith("O limite do seu cartão é calculado conforme sua margem disponível. \nPara solicitar o aumento de lim")):
            return False
    
        if not (messagesClient[31]["sender"] == "bot" and messagesClient[31]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[33]["sender"] == "bot" and messagesClient[33]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adiciona")):
            return False
    
        if not (messagesClient[35]["sender"] == "bot" and messagesClient[35]["message"].startswith("O Mastercard® Surpreenda é o programa de benefícios da Mastercard que oferece 1 ponto a cada compra ")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 1',
            "customerJourney": 'Acima de 8 opções no menu',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
    