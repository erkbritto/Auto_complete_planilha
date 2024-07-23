from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 1fd07465cb394409a7b4c40991989f3d

class Analyzer10 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 26):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!\n\nSou o Al\u00ea, seu assisten")):
            return False

        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("\u00d3timo. Em que posso ajudar?\n\u3164 *Digite a op\u00e7\u00e3o de")):
            return False

        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("*Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Bloqueio\n2 - Desblo")):
            return False

        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("Para efetuar o desbloqueio do seu cart\u00e3o, NIO Digital, precisamo")):
            return False

        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("Qual o nome completo da sua m\u00e3e?")):
            return False

        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("Qual a sua data de nascimento? (dd/mm/aaaa)")):
            return False

        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("N\u00e3o conseguimos validar as informa\u00e7\u00f5es fornecidas, pod")):
            return False

        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("Qual o nome completo da sua m\u00e3e?")):
            return False

        if not (messagesBot[17]["sender"] == "bot" and messagesBot[17]["message"].startswith("Qual a sua data de nascimento? (dd/mm/aaaa)")):
            return False

        if not (messagesBot[19]["sender"] == "bot" and messagesBot[19]["message"].startswith("N\u00e3o conseguimos validar as informa\u00e7\u00f5es fornecidas, pod")):
            return False

        if not (messagesBot[21]["sender"] == "bot" and messagesBot[21]["message"].startswith("*Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Limite dispon\u00edv")):
            return False

        if not (messagesBot[23]["sender"] == "bot" and messagesBot[23]["message"].startswith("*Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Bloqueio\n2 - Desblo")):
            return False

        if not (messagesBot[25]["sender"] == "bot" and messagesBot[25]["message"].startswith("S\u00f3 um momento enquanto te transferimos para um de nossos agentes")):
            return False

        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 3',
            "customerJourney": 'Selecionou 4 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }