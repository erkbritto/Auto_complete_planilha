from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 41a9df3253664978a5a4604744e10d0a

class Analyzer9 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 12):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!\n\nSou o Al\u00ea, seu assistent")):
            return False

        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("\u00d3timo. Em que posso ajudar?\n\u3164 *Digite a op\u00e7\u00e3o des")):
            return False

        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("Devido a um problema t\u00e9cnico na gera\u00e7\u00e3o das faturas, es")):
            return False

        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("*Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Limite dispon\u00edve")):
            return False

        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("Digite:\n\n1 - Dificuldade em efetuar compras com o cart\u00e3o.\n2 - ")):
            return False

        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("S\u00f3 um momento enquanto te transferimos para um de nossos agentes.")):
            return False


        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 10',
            "customerJourney": 'Selecionou 3 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }