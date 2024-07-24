from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# ID AQUI (70f62ed74c894ad9a118d2213c694aab)--> id não encontrado

class Analyzer1 :
    def isValid(
        self,
        messagesUSER: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesUSER) == 10):
            return False

        if not (messagesUSER[0]["sender"] == "client" and messagesUSER[0]["message"].startswith("")):
            return False

        if not (messagesUSER[2]["sender"] == "client" and messagesUSER[2]["message"].startswith("")):
            return False

        if not (messagesUSER[4]["sender"] == "client" and messagesUSER[4]["message"].startswith("")):
            return False

        if not (messagesUSER[6]["sender"] == "client" and messagesUSER[6]["message"].startswith("")):
            return False

        if not (messagesUSER[8]["sender"] == "client" and messagesUSER[8]["message"].startswith("")):
            return False
        
        if not (messagesUSER[10]["sender"] == "client" and messagesUSER[10]["message"].startswith("")):
            return False

        return True

    def getQualifications(
            self,
            messagesUSER: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 0',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'nao qualificado',
        }