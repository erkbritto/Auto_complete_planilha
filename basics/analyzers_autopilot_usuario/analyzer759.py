from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 9eaff5a6df414ccdaf4a55b105be8985

class Analyzer759 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 30):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adiciona")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("Para efetuar o desbloqueio do seu cartão, NIO Digital, precisamos que nos forneça algumas informaçõe")):
            return False
    
        if not (messagesClient[9]["sender"] == "bot" and messagesClient[9]["message"].startswith("Qual o nome completo da sua mãe?")):
            return False
    
        if not (messagesClient[11]["sender"] == "bot" and messagesClient[11]["message"].startswith("Qual a sua data de nascimento? (dd/mm/aaaa)")):
            return False
    
        if not (messagesClient[13]["sender"] == "bot" and messagesClient[13]["message"].startswith("Não conseguimos validar as informações fornecidas, pode por favor nos fornecer as seguintes informaç")):
            return False
    
        if not (messagesClient[15]["sender"] == "bot" and messagesClient[15]["message"].startswith("Qual o nome completo da sua mãe?")):
            return False
    
        if not (messagesClient[17]["sender"] == "bot" and messagesClient[17]["message"].startswith("Qual a sua data de nascimento? (dd/mm/aaaa)")):
            return False
    
        if not (messagesClient[19]["sender"] == "bot" and messagesClient[19]["message"].startswith("Não conseguimos validar as informações fornecidas, pode por favor nos fornecer as seguintes informaç")):
            return False
    
        if not (messagesClient[21]["sender"] == "bot" and messagesClient[21]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesClient[23]["sender"] == "bot" and messagesClient[23]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[25]["sender"] == "bot" and messagesClient[25]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesClient[27]["sender"] == "bot" and messagesClient[27]["message"].startswith("Seguem as informações solicitadas")):
            return False
    
        if not (messagesClient[29]["sender"] == "bot" and messagesClient[29]["message"].startswith("Tudo bem!\nNio Digital agradece e até logo!")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 3',
            "customerJourney": 'Selecionou 3 opções do menu',
            "finalizationOfTheContract": 'Contato encerrado com script de finalização.',
        }
    