from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 632f95ecb2754841bfca8ae959148736

class Analyzer3 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 16):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False

        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("N\u00e3o conseguimos localizar o CPF i")):
            return False

        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("\u00d3timo. Em que posso ajudar?\n\u3164")):
            return False

        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("*Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Bloqueio\n2")):
            return False

        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("Para efetuar o desbloqueio do seu cart")):
            return False

        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("Qual o nome completo da sua m\u00e3e?")):
            return False

        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("Qual a sua data de nascimento? (dd/mm/")):
            return False

        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("No momento n\u00e3o conseguimos realiz")):
            return False

        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 3',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }
