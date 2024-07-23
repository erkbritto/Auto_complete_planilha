from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# a85f5fb72fe348cdb55ecfb99812cd31

class Analyzer143 :

    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 42):
            return False
    
        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("Por favor informe os 4 últimos dígitos do cartão que deseja consultar.")):
            return False
    
        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("Seguem as informações solicitadas:")):
            return False
    
        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adiciona")):
            return False
    
        if not (messagesBot[17]["sender"] == "bot" and messagesBot[17]["message"].startswith("Para efetuar o desbloqueio do seu cartão, NIO Digital, precisamos que nos forneça algumas informaçõe")):
            return False
    
        if not (messagesBot[19]["sender"] == "bot" and messagesBot[19]["message"].startswith("Qual o nome completo da sua mãe?")):
            return False
    
        if not (messagesBot[21]["sender"] == "bot" and messagesBot[21]["message"].startswith("Qual a sua data de nascimento? (dd/mm/aaaa)")):
            return False
    
        if not (messagesBot[23]["sender"] == "bot" and messagesBot[23]["message"].startswith("Não conseguimos validar as informações fornecidas, pode por favor nos fornecer as seguintes informaç")):
            return False
    
        if not (messagesBot[25]["sender"] == "bot" and messagesBot[25]["message"].startswith("Qual o nome completo da sua mãe?")):
            return False
    
        if not (messagesBot[27]["sender"] == "bot" and messagesBot[27]["message"].startswith("Qual a sua data de nascimento? (dd/mm/aaaa)")):
            return False
    
        if not (messagesBot[29]["sender"] == "bot" and messagesBot[29]["message"].startswith("Não conseguimos validar as informações fornecidas, pode por favor nos fornecer as seguintes informaç")):
            return False
    
        if not (messagesBot[31]["sender"] == "bot" and messagesBot[31]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesBot[33]["sender"] == "bot" and messagesBot[33]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adiciona")):
            return False
    
        if not (messagesBot[35]["sender"] == "bot" and messagesBot[35]["message"].startswith("Para efetuar o desbloqueio do seu cartão, NIO Digital, precisamos que nos forneça algumas informaçõe")):
            return False
    
        if not (messagesBot[37]["sender"] == "bot" and messagesBot[37]["message"].startswith("Qual o nome completo da sua mãe?")):
            return False
    
        if not (messagesBot[39]["sender"] == "bot" and messagesBot[39]["message"].startswith("Qual a sua data de nascimento? (dd/mm/aaaa)")):
            return False
    
        if not (messagesBot[41]["sender"] == "bot" and messagesBot[41]["message"].startswith("No momento não conseguimos realizar o desbloqueio do seu cartão, mas não se preocupe, estou vou tran")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 1',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }
    