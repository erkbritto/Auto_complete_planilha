from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 1bee58e73f1b4ee3af71b449dbc6af3d

class Analyzer7 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 2):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Encontramos uma dificuldade em entender a sua solicita\u00e7\u00e3o. Vou transferir")):
            return False

        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'nao qualificado',
        }
