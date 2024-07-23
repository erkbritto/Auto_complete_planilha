from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# f37194814e18448d86b4b2bdf1d7d3c6

class Analyzer24 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        return False
        if not (len(messagesBot) == 16):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False

        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("N\u00e3o conseguimos localizar o CPF informado")):
            return False

        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("\u00d3timo. Em que posso ajudar?")):
            return False

        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("Por favor informe os 4 \u00faltimos")):
            return False

        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("*Tudo bem. Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Valor m\u00ednimo")):
            return False

        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("*Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Limite dispon\u00edvel")):
            return False

        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("Digite:\n\n1 - Dificuldade em efetuar compras com o cart\u00e3o.\n2 - Outros assuntos.\n3 - Retornar ao menu anterior.")):
            return False

        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("S\u00f3 um momento enquanto te transferimos para um de nossos agentes.")):
            return False

        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": 'nao qualificado',
        }
