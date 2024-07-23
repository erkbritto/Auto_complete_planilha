from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 4aec84ef3845466b9a814f54084f4a64

class Analyzer6 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 8):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!\n\nSou o Al\u00ea, seu assistente")):
            return False

        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("\u00d3timo. Em que posso ajudar?\n\u3164 *Digite a op\u00e7\u00e3o dese")):
            return False

        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("Digite:\n\n1 - Dificuldade em efetuar compras com o cart\u00e3o.\n2 - O")):
            return False

        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("S\u00f3 um momento enquanto te transferimos para um de nossos agentes.")):
            return False

        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 0',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }