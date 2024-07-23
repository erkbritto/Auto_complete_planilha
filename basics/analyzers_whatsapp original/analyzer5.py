from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# b41abda22d8141b6b6c5cf4b7f706b11

class Analyzer5 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 28):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False

        if not (messagesBot[3]["sender"] == "bot" and messagesBot[3]["message"].startswith("\u00d3timo. Em que posso ajudar?")):
            return False

        if not (messagesBot[5]["sender"] == "bot" and messagesBot[5]["message"].startswith("*Digite a op\u00e7\u00e3o desejada pa")):
            return False

        if not (messagesBot[7]["sender"] == "bot" and messagesBot[7]["message"].startswith("Para efetuar o desbloqueio do seu car")):
            return False

        if not (messagesBot[9]["sender"] == "bot" and messagesBot[9]["message"].startswith("Qual o nome completo da sua m\u00e3e?")):
            return False

        if not (messagesBot[11]["sender"] == "bot" and messagesBot[11]["message"].startswith("Qual a sua data de nascimento? (dd/mm")):
            return False

        if not (messagesBot[13]["sender"] == "bot" and messagesBot[13]["message"].startswith("N\u00e3o conseguimos validar as infor")):
            return False

        if not (messagesBot[15]["sender"] == "bot" and messagesBot[15]["message"].startswith("Qual o nome completo da sua m\u00e3e?")):
            return False


        if not (messagesBot[17]["sender"] == "bot" and messagesBot[17]["message"].startswith("Qual a sua data de nascimento? (dd/mm")):
            return False


        if not (messagesBot[19]["sender"] == "bot" and messagesBot[19]["message"].startswith("N\u00e3o conseguimos validar as infor")):
            return False


        if not (messagesBot[21]["sender"] == "bot" and messagesBot[21]["message"].startswith("*Digite a op\u00e7\u00e3o desejada pa")):
            return False


        if not (messagesBot[23]["sender"] == "bot" and messagesBot[23]["message"].startswith("Digite:\n\n1 - Dificuldade em efetuar")):
            return False


        if not (messagesBot[25]["sender"] == "bot" and messagesBot[25]["message"].startswith("Desculpe, n\u00e3o entendi sua solici")):
            return False


        if not (messagesBot[27]["sender"] == "bot" and messagesBot[27]["message"].startswith("S\u00f3 um momento enquanto te transf")):
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