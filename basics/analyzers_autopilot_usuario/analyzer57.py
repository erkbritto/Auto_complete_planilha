from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# c19b9685525c433a9e71b05950e60553

class Analyzer57 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 2):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
    