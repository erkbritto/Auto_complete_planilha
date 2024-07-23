from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 8d71804c770a4654be4175f04318beee

class Analyzer4 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 16):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!\n\nSou o Al\u00ea, seu as")):
            return False

        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("N\u00e3o conseguimos localizar o CPF informado, digite-o novame")):
            return False

        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("\u00d3timo. Em que posso ajudar?\n\u3164 *Digite a op")):
            return False

        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("Por favor informe os 4 \u00faltimos d\u00edgitos do cart\u00e3o")):
            return False

        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("O \u00faltimos 4 d\u00edgitos que voc\u00ea digitou est\u00e1 i")):
            return False

        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("*Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Limite dispon")):
            return False

        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("Digite:\n\n1 - Dificuldade em efetuar compras com o cart\u00e3o")):
            return False

        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("S\u00f3 um momento enquanto te transferimos para um de nossos a")):
            return False

        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 3 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }